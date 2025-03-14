from .utils import identity as _


def get_custom_fields():
	return {
		"Item": [
			{
				"fieldname": "custom_is_element",
				"label": _("Is Element"),
				"insert_after": "has_variants",
				"fieldtype": "Check",
				"search_index": 1,
			},
			{
				"fieldname": "custom_is_container",
				"label": _("Is Container"),
				"insert_after": "custom_is_element",
				"fieldtype": "Check",
				"search_index": 1,
			},
		],
		"Quotation": [
			{
				"fieldname": "custom_project",
				"label": _("Project"),
				"insert_after": "company",
				"fieldtype": "Link",
				"options": "Project",
				"in_standard_filter": 1,
				"search_index": 1,
			}
		],
		("Quotation Item", "Sales Order Item", "Sales Invoice Item"): [
			{
				"fieldname": "custom_parent_line_idx",
				"label": _("Parent Line Index"),
				"insert_after": "item_name",
				"fieldtype": "Int",
				"non_negative": 1,
			},
			{
				"fieldname": "custom_is_inclusive",
				"label": _("Is Inclusive"),
				"insert_after": "custom_parent_line_idx",
				"fieldtype": "Check",
			},
			{
				"fieldname": "custom_building",
				"label": _("Building"),
				"insert_after": "custom_is_inclusive",
				"fieldtype": "Data",
			},
			{
				"fieldname": "custom_section",
				"label": _("Section"),
				"insert_after": "custom_building",
				"fieldtype": "Data",
			},
		],
		"Delivery Note Item": [
			{
				"fieldname": "custom_parent_line_idx",
				"label": _("Parent Line Index"),
				"insert_after": "item_name",
				"fieldtype": "Int",
				"non_negative": 1,
			},
			{
				"fieldname": "custom_is_inclusive",
				"label": _("Is Inclusive"),
				"insert_after": "custom_parent_line_idx",
				"fieldtype": "Check",
			},
			{
				"fieldname": "custom_building",
				"label": _("Building"),
				"insert_after": "custom_is_inclusive",
				"fieldtype": "Data",
			},
			{
				"fieldname": "custom_section",
				"label": _("Section"),
				"insert_after": "custom_building",
				"fieldtype": "Data",
			},
			{
				"fieldname": "custom_ahead_delivery_no",
				"label": _("Ahead Delivery No."),
				"insert_after": "custom_section",
				"fieldtype": "Data",
				"search_index": 1,
			},
			{
				"fieldname": "custom_ahead_delivery_line_no",
				"label": _("Ahead Delivery Line No."),
				"insert_after": "custom_ahead_delivery_no",
				"fieldtype": "Data",
				"search_index": 1,
			},
			{
				"fieldname": "custom_element_no",
				"label": _("Element No."),
				"insert_after": "custom_ahead_delivery_line_no",
				"fieldtype": "Data",
				"search_index": 1,
			},
		],
		"Sales Order": [
			{
				"fieldname": "custom_valid_till",
				"label": _("Valid Till"),
				"insert_after": "po_no",
				"fieldtype": "Date",
				"in_standard_filter": 1,
				"search_index": 1,
			}
		],
		"Delivery Note": [
			{
				"fieldname": "custom_sales_order",
				"label": _("Sales Order"),
				"insert_after": "company",
				"fieldtype": "Link",
				"options": "Sales Order",
				"in_standard_filter": 1,
				"search_index": 1,
			},
		],
		"Sales Invoice": [
			{
				"fieldname": "custom_sales_order",
				"label": _("Sales Order"),
				"insert_after": "company_tax_id",
				"fieldtype": "Link",
				"options": "Sales Order",
				"in_standard_filter": 1,
				"search_index": 1,
			},
			{
				"fieldname": "custom_ahead_invoice_plan_id",
				"label": _("Ahead Invoice Plan ID"),
				"insert_after": "custom_sales_order",
				"fieldtype": "Data",
				"search_index": 1,
			},
		],
	}
