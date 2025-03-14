import frappe


def execute():
	# Delete the custom field
	frappe.delete_doc_if_exists("Custom Field", "Delivery Note-custom_ahead_delivery_no")

	# Drop the column from Delivery Note if it exists
	frappe.db.sql(
		"""
        ALTER TABLE `tabDelivery Note`
        DROP COLUMN IF EXISTS `custom_ahead_delivery_no`;
    """
	)
