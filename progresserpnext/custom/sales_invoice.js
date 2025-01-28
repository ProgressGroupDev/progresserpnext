frappe.ui.form.on("Sales Invoice", {
	setup: function (frm) {
		frm.set_query("custom_sales_order", function (doc) {
			return {
				filters: {
					company: doc.company,
				},
			};
		});
	},
});
