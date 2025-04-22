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
			fieldname: "company",
			label: "Company",
			fieldtype: "Link",
			options: "Company",
		},
		{
			fieldname: "warehouse",
			label: "Warehouse",
			fieldtype: "Link",
			options: "Warehouse",
			get_query: () => {
				const company = frappe.query_report.get_filter_value("company");

				if (!company) {
					return {};
				}

				return {
					filters: {
						company: company,
					},
				};
			},
		},
	],
};
