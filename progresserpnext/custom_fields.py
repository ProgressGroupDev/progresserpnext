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
		("Quotation Item", "Sales Order Item", "Sales Invoice Item", "Delivery Note Item"): [
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
		"Sales Order": [
			{
				"fieldname": "custom_quotation",
				"label": _("Quotation"),
				"insert_after": "po_no",
				"fieldtype": "Link",
				"options": "Quotation",
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
			}
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
			}
		],
	}
