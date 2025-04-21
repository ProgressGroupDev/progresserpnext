# Copyright (c) 2025, Progress Software Development GmbH and contributors
# For license information, please see license.txt

import frappe
from erpnext.stock.doctype.serial_and_batch_bundle.serial_and_batch_bundle import (
	get_auto_batch_nos,
)
from frappe import _
from frappe.utils.data import flt


def execute(filters=None):
	return get_columns(filters), get_data(filters)


def get_data(filters):
	results = []
	for bin in frappe.get_all(
		"Bin",
		filters=filters,
		fields=[
			"item_code",
			"warehouse",
			"actual_qty",
			"stock_uom",
			"stock_value",
		],
	):
		results.append(bin)
		has_serial_no, has_batch_no = frappe.db.get_value(
			"Item", bin.item_code, ["has_serial_no", "has_batch_no"]
		)
		if has_serial_no:
			serial_nos = frappe.get_all(
				"Serial No",
				filters={"item_code": bin.item_code, "warehouse": bin.warehouse, "status": "Active"},
				fields=["serial_no", "batch_no"],
			)
			results.extend(
				[
					{
						"indent": 1,
						"warehouse": bin.warehouse,
						"serial_no": serial_no.serial_no,
						"batch_no": serial_no.batch_no,
						"actual_qty": 1,
						"stock_uom": bin.stock_uom,
						"stock_value": flt(bin.stock_value / bin.actual_qty, 2) if bin.actual_qty else 0,
					}
					for serial_no in serial_nos
				]
			)

		if has_batch_no and not has_serial_no:
			batch_qty = get_auto_batch_nos(
				kwargs=frappe._dict(
					warehouse=bin.warehouse,
					item_code=bin.item_code,
					for_stock_levels=True,
				)
			)
			results.extend(
				[
					{
						"indent": 1,
						"warehouse": bin.warehouse,
						"batch_no": batch.batch_no,
						"actual_qty": batch.qty,
						"stock_uom": bin.stock_uom,
						"stock_value": (
							flt(bin.stock_value / bin.actual_qty * batch.qty, 2) if bin.actual_qty else 0
						),
					}
					for batch in batch_qty
				]
			)

	return results


def get_columns(filters):
	columns = [
		{
			"fieldname": "item_code",
			"fieldtype": "Link",
			"options": "Item",
			"label": _("Item Code"),
			"width": 200,
		},
		{
			"fieldname": "serial_no",
			"fieldtype": "Link",
			"options": "Serial No",
			"label": _("Serial No"),
			"width": 120,
		},
		{
			"fieldname": "batch_no",
			"fieldtype": "Link",
			"options": "Batch",
			"label": _("Batch No"),
			"width": 120,
		},
		{
			"fieldname": "warehouse",
			"fieldtype": "Link",
			"options": "Warehouse",
			"label": _("Warehouse"),
			"width": 180,
		},
		{
			"fieldname": "actual_qty",
			"fieldtype": "Float",
			"label": _("Actual Qty"),
			"width": 120,
		},
		{
			"fieldname": "stock_uom",
			"fieldtype": "Link",
			"options": "UOM",
			"label": _("UOM"),
			"width": 120,
		},
		{
			"fieldname": "stock_value",
			"fieldtype": "Currency",
			"label": _("Stock Value"),
			"width": 120,
		},
	]

	if filters.get("warehouse"):
		columns = [column for column in columns if column["fieldname"] != "warehouse"]

	if filters.get("item_code"):
		columns = [column for column in columns if column["fieldname"] != "item_code"]

	return columns
