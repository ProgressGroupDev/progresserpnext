from typing import TYPE_CHECKING

import frappe
from erpnext.stock.doctype.serial_and_batch_bundle.serial_and_batch_bundle import (
	get_available_batches,
)
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


def before_validate(doc: "DeliveryNote", event: str):
	guess_warehouse(doc)


def guess_warehouse(doc: "DeliveryNote"):
	"""When new item lines are added to a delivery note, prefill the current storage
	location of certain items automatically:

	- If the item is marked as “Element” and batch traceable, use the itemno.
		and the batch no. to find the element on stock. Use the found warehouse
		in the delivery line. If no stock entry is found, let ERPNext use the
		default warehouse set in the item master data.
	- If the item is marked as “Container” and serialized, use the item no.
		and the serial no. to find the container on stock. Use the found
		warehouse in the delivery line. If no stock entry is found, let ERPNext
		use the default warehouse set in the item master data.
	- If the item is not marked as “Element” or “Container,” don't apply these
		logics. Then the warehouse will be filled by ahead, or if not, the
		default warehouse of the item is applied automatically by ERPNext
	"""
	if doc.is_return:
		return

	for line_item in doc.items:
		if not line_item.item_code:
			continue

		if line_item.warehouse:
			continue

		item = frappe.get_doc("Item", line_item.item_code)
		if not item.custom_is_element and not item.custom_is_container:
			# Item is neither element nor container, warehouse will be filled by ahead
			continue

		if item.custom_is_element and item.has_batch_no and line_item.batch_no:
			batches = get_available_batches(
				frappe._dict(
					posting_date=doc.posting_date,
					posting_time=doc.posting_time,
					item_code=line_item.item_code,
					batch_no=line_item.batch_no,
				)
			)
			line_item.warehouse = next(
				(batch.warehouse for batch in batches if batch.qty >= line_item.qty),
				None,
			)
		elif item.custom_is_container and item.has_serial_no and line_item.serial_no:
			warehouses = get_warehouses(line_item.serial_no, line_item.item_code)
			if len(warehouses) > 1:
				frappe.throw(
					_(
						"Row #{0}: The given serial nos are located in different warehouses. Please create a separate row per warehouse."
					).format(line_item.idx)
				)
			elif len(warehouses) == 1:
				line_item.warehouse = warehouses[0]

		if not line_item.warehouse:
			line_item.warehouse = next(
				(row.default_warehouse for row in item.item_defaults if row.company == doc.company),
				None,
			)


def get_warehouses(serial_nos: str, item_code: str) -> list[str]:
	serial_nos = [sn.strip() for sn in serial_nos.split("\n") if sn]
	return frappe.get_all(
		"Serial No",
		filters={"serial_no": ("in", serial_nos), "item_code": item_code},
		pluck="warehouse",
		distinct=True,
	)
