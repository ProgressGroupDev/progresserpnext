frappe.ui.form.on("Sales Order", {
	setup: function (frm) {
		frm.set_query("custom_quotation", function (doc) {
			return {
				filters: {
					company: doc.company,
				},
			};
		});
	},
});
