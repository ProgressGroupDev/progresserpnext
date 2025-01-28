from typing import TYPE_CHECKING

import frappe
from frappe import _

if TYPE_CHECKING:
	from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice


def before_save(doc: "SalesInvoice", event: str):
	if not doc.custom_sales_order:
		linked_sales_orders = {row.sales_order for row in doc.items if row.sales_order}
		if len(linked_sales_orders) == 1:
			doc.custom_sales_order = linked_sales_orders.pop()


def validate(doc: "SalesInvoice", event: str):
	linked_sales_orders = {row.sales_order for row in doc.items if row.sales_order}
	if len(linked_sales_orders) > 1:
		frappe.throw(
			_(
				"The rows of this sales invoice are linked to different sales orders. Please link only one sales order."
			)
		)
