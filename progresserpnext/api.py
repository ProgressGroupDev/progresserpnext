import frappe


@frappe.whitelist(methods=["POST"])
def dry_run(doc: dict, action: str) -> dict:
	doc = frappe.get_doc(doc)
	doc.check_permission()
	doc.run_method(action)

	result = doc.as_dict(convert_dates_to_str=True, no_private_properties=True)

	frappe.db.rollback()

	return result
