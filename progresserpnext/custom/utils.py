from typing import TYPE_CHECKING

import frappe
from frappe import _

if TYPE_CHECKING:
	from erpnext.controllers.selling_controller import SellingController


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
