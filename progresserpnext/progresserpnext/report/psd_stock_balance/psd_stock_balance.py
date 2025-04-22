# Copyright (c) 2025, Progress Software Development GmbH and contributors
# For license information, please see license.txt

import frappe
from erpnext.stock.doctype.serial_and_batch_bundle.serial_and_batch_bundle import (
	get_auto_batch_nos,
)
from frappe import _
from frappe.utils.data import flt


def execute(filters: dict):
	return get_columns(filters.copy()), get_data(filters.copy())


def get_filters_list(filters: dict) -> list[list]:
	"""Turn the filters dict into a list.

	The conversion is necessary to allow multiple filters on warehouse.

	- If the warehouse in the dict is a group warehouse, add the 'descendants of (inclusive)'
	filter to the list. Else, add the '=' filter.
	- If an item code filter is present in the dict, add it to the list.
	- If a company filter is present in the dict, add a filter to the list to only include
	warehouses for that company. The company filter itself is not added to the list.
	"""
	filters_list = []

	warehouse = filters.get("warehouse")
	if warehouse:
		if frappe.db.get_value("Warehouse", warehouse, "is_group"):
			filters_list.append(["warehouse", "descendants of (inclusive)", warehouse])
		else:
			filters_list.append(["warehouse", "=", warehouse])

	item = filters.get("item_code")
	if item:
		filters_list.append(["item_code", "=", item])

	company = filters.get("company")
	if company:
		warehouses = frappe.db.get_all("Warehouse", filters={"company": company}, pluck="name", distinct=True)
		filters_list.append(["warehouse", "in", warehouses])

	return filters_list


def get_data(filters: dict) -> list[dict]:
	results = []
	for bin in frappe.get_all(
		"Bin",
		filters=get_filters_list(filters),
		fields=[
			"item_code",
			"warehouse",
			"actual_qty",
			"stock_uom",
			"stock_value",
		],
	):
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
						"item_code": bin.item_code,
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
			bin["actual_qty"] -= len(serial_nos)

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
						"item_code": bin.item_code,
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
			bin["actual_qty"] -= sum(batch.qty for batch in batch_qty)

		if bin["actual_qty"]:
			results.append(bin)

	return results


def get_columns(filters: dict):
	return [
		{
			"fieldname": "item_code",
			"fieldtype": "Link",
			"options": "Item",
			"label": _("Item Code"),
			"width": 180,
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
