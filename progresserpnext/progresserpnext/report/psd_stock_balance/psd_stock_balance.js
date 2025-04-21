// Copyright (c) 2025, Progress Software Development GmbH and contributors
// For license information, please see license.txt

frappe.query_reports["PSD Stock Balance"] = {
	filters: [
		{
			fieldname: "item_code",
			label: "Item Code",
			fieldtype: "Link",
			options: "Item",
		},
		{
			fieldname: "warehouse",
			label: "Warehouse",
			fieldtype: "Link",
			options: "Warehouse",
		},
	],
};
