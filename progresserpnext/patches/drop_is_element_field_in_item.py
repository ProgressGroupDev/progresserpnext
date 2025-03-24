import frappe


def execute():
	# Delete the custom field
	frappe.delete_doc_if_exists("Custom Field", "Item-custom_is_element")

	# Drop the column if it exists
	frappe.db.sql_ddl(
		"""
        ALTER TABLE `tabItem`
        DROP COLUMN IF EXISTS `custom_is_element`;
    """
	)
