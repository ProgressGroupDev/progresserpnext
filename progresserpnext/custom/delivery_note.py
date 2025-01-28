from typing import TYPE_CHECKING

import frappe
from frappe import _

if TYPE_CHECKING:
	from erpnext.stock.doctype.delivery_note.delivery_note import DeliveryNote


def before_save(doc: "DeliveryNote", event: str):
	if not doc.custom_sales_order:
		linked_sales_orders = {row.against_sales_order for row in doc.items if row.against_sales_order}
		if len(linked_sales_orders) == 1:
			doc.custom_sales_order = linked_sales_orders.pop()


def validate(doc: "DeliveryNote", event: str):
	linked_sales_orders = {row.against_sales_order for row in doc.items if row.against_sales_order}
	if len(linked_sales_orders) > 1:
		frappe.throw(
			_(
				"The rows of this delivery note are linked to different sales orders. Please link only one sales order."
			)
		)
