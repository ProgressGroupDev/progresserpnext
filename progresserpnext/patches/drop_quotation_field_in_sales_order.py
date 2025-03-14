import frappe


def execute():
	# Delete the custom field
	frappe.delete_doc_if_exists("Custom Field", "Sales Order-custom_quotation")

	# Drop the column from Sales Order if it exists
	frappe.db.sql(
		"""
        ALTER TABLE `tabSales Order`
        DROP COLUMN IF EXISTS `custom_quotation`;
    """
	)
