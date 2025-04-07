import frappe
from erpnext.controllers.accounts_controller import get_default_taxes_and_charges, update_child_qty_rate


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
def dry_run_no_validation(doc: dict, action: str) -> dict:
	doc = frappe.get_doc(doc)
	doc.flags.ignore_permissions = True
	doc.flags.ignore_mandatory = True
	doc.flags.ignore_links = True
	doc.flags.dont_notify = True
	doc.flags.ignore_on_update = True
	doc.flags.ignore_validate_update_after_submit = True
	doc.flags.ignore_version = True
	doc.flags.no_email = True
	doc.run_method(action)

	result = doc.as_dict(convert_dates_to_str=True, no_private_properties=True)

	frappe.db.rollback()

	return result


@frappe.whitelist(methods=["POST"])
def dry_run_calculate_taxes_and_totals(doc: dict) -> dict:
	doc = frappe.get_doc(doc)

	doc.calculate_taxes_and_totals()

	return doc.as_dict(convert_dates_to_str=True, no_private_properties=True)
