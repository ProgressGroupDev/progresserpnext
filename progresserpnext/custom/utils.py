from typing import TYPE_CHECKING

import frappe
from frappe import _
from frappe.utils.data import flt

if TYPE_CHECKING:
	from erpnext.controllers.selling_controller import SellingController


def calculate_sales_valuation_and_margin(doc: "SellingController", event: str):
	"""Calculate Sales Valuation Rate and Margin for each line item and for header."""

	for item in doc.items:
		use_standard_price, standard_valuation_rate, valuation_rate = frappe.db.get_value(
			"Item",
			item.item_code,
			["custom_use_standard_price", "custom_standard_valuation_rate", "valuation_rate"],
		)

		if use_standard_price:
			item.custom_sales_valuation_rate = flt(standard_valuation_rate)
		else:
			item.custom_sales_valuation_rate = flt(valuation_rate)

	calculate_line_margins(doc)

	calculate_header_margins(doc)


def calculate_line_margins(doc: "SellingController"):
	"""Calculate margin % and margin absolute for each main sales line."""

	for item in doc.items:
		if item.custom_parent_line_idx and item.custom_parent_line_idx:
			item.custom_margin_abs = 0
			item.custom_margin_percent = 0
			continue

		inclusive_items = [
			sub_item
			for sub_item in doc.items
			if sub_item.custom_parent_line_idx == item.idx and sub_item.custom_is_inclusive
		]

		total_cost = (item.custom_sales_valuation_rate * item.qty) + sum(
			sub.custom_sales_valuation_rate * sub.qty for sub in inclusive_items
		)

		item.custom_margin_abs = item.amount - total_cost

		item.custom_margin_percent = (item.custom_margin_abs / item.amount * 100) if item.amount > 0 else 0


def calculate_header_margins(doc: "SellingController"):
	"""Calculate Margin % and Margin Abs. at the header level."""

	if not doc.net_total:
		return

	cost_sum = 0
	for item in doc.items:
		cost_sum += item.custom_sales_valuation_rate * item.qty

	doc.custom_margin_percent = (doc.net_total - cost_sum) / doc.net_total * 100 if doc.net_total != 0 else 0

	doc.custom_margin_abs = doc.net_total - cost_sum


def validate_parent_line_idx(doc: "SellingController", event: str):
	"""Ensure that the parent line index is a valid row number."""
	if not doc.items:
		return

	num_rows = len(doc.items)
	for row in doc.items:
		if not row.custom_parent_line_idx:
			continue

		if row.custom_parent_line_idx > num_rows:
			frappe.throw(_("Parent line index must not be greater than the number of rows."))

		if row.custom_parent_line_idx == row.idx:
			frappe.throw(_("Parent line index must not be the same as the current line index."))
