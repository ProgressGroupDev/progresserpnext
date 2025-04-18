import frappe


def execute():
	# Delete the custom fields
	frappe.delete_doc_if_exists("Custom Field", "Item-custom_is_delivery_item")
	frappe.delete_doc_if_exists("Custom Field", "Item-custom_use_standard_pricee")

	# Drop the columns if they exist

	frappe.db.sql_ddl(
		"""
        ALTER TABLE `tabItem`
        DROP COLUMN IF EXISTS `custom_is_delivery_item`;
        """
	)

	frappe.db.sql_ddl(
		"""
        ALTER TABLE `tabItem`
        DROP COLUMN IF EXISTS `custom_use_standard_pricee`;
        """
	)
