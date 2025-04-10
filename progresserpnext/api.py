import json

import frappe
from erpnext.controllers.accounts_controller import get_default_taxes_and_charges, update_child_qty_rate
from frappe.desk.form.save import savedocs


@frappe.whitelist(methods=["POST"])
def dry_run(doc: dict, action: str) -> dict:
	doc = frappe.get_doc(doc)
	doc.check_permission()
	doc.run_method(action)

	result = doc.as_dict(convert_dates_to_str=True, no_private_properties=True)

	frappe.db.rollback()

	return result


@frappe.whitelist(methods=["GET"])
def get_sales_order_defaults():
	frappe.has_permission("Sales Order", "create", throw=True)

	user_defaults = frappe.defaults.get_defaults()
	company = user_defaults.get("company")
	currency = user_defaults.get("currency")
	price_list = user_defaults.get("selling_price_list") or user_defaults.get("price_list")

	default_taxes = get_default_taxes_and_charges("Sales Taxes and Charges Template", "", company)

	frappe.response.update(
		{
			"data": {
				"company": company,
				"currency": currency,
				"price_list": price_list,
				"sales_taxes_and_charges_template": default_taxes.get("taxes_and_charges"),
			}
		}
	)


@frappe.whitelist(methods=["POST"])
def dry_run_update_items(
	doc: dict, parent_doctype, trans_items, parent_doctype_name, child_docname="items"
) -> dict:
	doc = frappe.get_doc(doc)
	doc.check_permission()

	update_child_qty_rate(parent_doctype, trans_items, parent_doctype_name, child_docname=child_docname)

	updated_doc = frappe.get_doc(parent_doctype, parent_doctype_name)
	result = updated_doc.as_dict(convert_dates_to_str=True, no_private_properties=True)

	frappe.db.rollback()
	return result


@frappe.whitelist(methods=["POST"])
def dry_run_calculate_taxes_and_totals(doc: dict) -> dict:
	doc = frappe.get_doc(doc)
	doc.check_permission()
	doc.calculate_taxes_and_totals()

	return doc.as_dict(convert_dates_to_str=True, no_private_properties=True)


@frappe.whitelist(methods=["POST"])
def update_submitted_sales_order(
	doc: dict, parent_doctype, trans_items, parent_doctype_name, child_docname="items"
) -> dict:
	"""Update Sales Order fields and save using `savedocs()` before updating child items."""

	if isinstance(trans_items, list):
		trans_items = json.dumps(trans_items)

	if isinstance(doc, str):
		doc = frappe.parse_json(doc)

	sales_order = frappe.get_doc("Sales Order", parent_doctype_name)
	sales_order.check_permission()

	allowed_fields = [
		"delivery_date",
		"po_no",
		"po_date",
		"customer_address",
		"shipping_address_name",
		"dispatch_address_name",
	]

	for field in allowed_fields:
		if field in doc:
			setattr(sales_order, field, doc[field])

	sales_order_json = frappe.as_json(sales_order)

	savedocs(sales_order_json, "Update")

	update_child_qty_rate(parent_doctype, trans_items, parent_doctype_name, child_docname=child_docname)

	updated_doc = frappe.get_doc(parent_doctype, parent_doctype_name)

	result = updated_doc.as_dict(convert_dates_to_str=True, no_private_properties=True)

	return result
