import frappe
from erpnext.controllers.accounts_controller import get_default_taxes_and_charges


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
    user_defaults = frappe.defaults.get_defaults()
    company = user_defaults.get("company")
    currency = user_defaults.get("currency")
    price_list = user_defaults.get("selling_price_list") or user_defaults.get("price_list")

    default_taxes = get_default_taxes_and_charges("Sales Taxes and Charges Template", "", company)

    return {
        "company": company,
        "currency": currency,
        "price_list": price_list,
        "sales_taxes_and_charges_template": default_taxes.get("taxes_and_charges"), 
    }