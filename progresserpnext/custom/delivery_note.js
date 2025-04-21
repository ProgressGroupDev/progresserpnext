frappe.ui.form.on("Delivery Note", {
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
