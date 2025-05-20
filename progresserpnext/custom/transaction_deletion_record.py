import frappe
from erpnext.setup.doctype.transaction_deletion_record.transaction_deletion_record import (
	TransactionDeletionRecord,
)
from frappe.model.document import Document


@frappe.whitelist()
def get_doctypes_to_be_ignored():
	doctypes_to_be_ignored = [
		"Account",
		"Cost Center",
		"Warehouse",
		"Budget",
		"Party Account",
		"Employee",
		"Sales Taxes and Charges Template",
		"Purchase Taxes and Charges Template",
		"POS Profile",
		"Company",
		"Bank Account",
		"Item Tax Template",
		"Mode of Payment",
		"Mode of Payment Account",
		"Item Default",
		"Customer",
		"Supplier",
		"Shipping Rule",
		"Department",
	]

	doctypes_to_be_ignored.extend(frappe.get_hooks("company_data_to_be_ignored") or [])

	return doctypes_to_be_ignored


class CustomTransactionDeletionRecord(TransactionDeletionRecord):
	def validate(self):
		pass

	def validate_doctypes_to_be_ignored(self):
		pass
