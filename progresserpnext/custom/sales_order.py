from typing import TYPE_CHECKING

import frappe
from frappe import _

if TYPE_CHECKING:
	from erpnext.selling.doctype.sales_order.sales_order import SalesOrder


def before_save(doc: "SalesOrder", event: str):
	if not doc.custom_quotation:
		linked_quotations = {row.prevdoc_docname for row in doc.items if row.prevdoc_docname}
		if len(linked_quotations) == 1:
			doc.custom_quotation = linked_quotations.pop()


def validate(doc: "SalesOrder", event: str):
	linked_quotations = {row.prevdoc_docname for row in doc.items if row.prevdoc_docname}
	if len(linked_quotations) > 1:
		frappe.throw(
			_(
				"The rows of this sales order are linked to different quotations. Please link only one quotation."
			)
		)
