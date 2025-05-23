app_name = "progresserpnext"
app_title = "progresserpnext"
app_publisher = "Progress Software Development GmbH"
app_description = "ERPNext Customizations for Progress Software Development GmbH"
app_email = "info@progress-psd.com"
app_license = "gpl-3.0"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "progresserpnext",
# 		"logo": "/assets/progresserpnext/logo.png",
# 		"title": "progresserpnext",
# 		"route": "/progresserpnext",
# 		"has_permission": "progresserpnext.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/progresserpnext/css/progresserpnext.css"
# app_include_js = "/assets/progresserpnext/js/progresserpnext.js"

# include js, css files in header of web template
# web_include_css = "/assets/progresserpnext/css/progresserpnext.css"
# web_include_js = "/assets/progresserpnext/js/progresserpnext.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "progresserpnext/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "progresserpnext/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "progresserpnext.utils.jinja_methods",
# 	"filters": "progresserpnext.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "progresserpnext.install.before_install"
after_install = "progresserpnext.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "progresserpnext.uninstall.before_uninstall"
# after_uninstall = "progresserpnext.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "progresserpnext.utils.before_app_install"
# after_app_install = "progresserpnext.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "progresserpnext.utils.before_app_uninstall"
# after_app_uninstall = "progresserpnext.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "progresserpnext.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }


# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Quotation": {
		"validate": [
			"progresserpnext.custom.utils.validate_parent_line_idx",
		],
		"before_save": [
			"progresserpnext.custom.utils.calculate_sales_valuation_and_margin",
		],
	},
	"Sales Order": {
		"validate": [
			"progresserpnext.custom.utils.validate_parent_line_idx",
		],
		"before_save": [
			"progresserpnext.custom.utils.calculate_sales_valuation_and_margin",
		],
	},
	"Sales Invoice": {
		"validate": [
			"progresserpnext.custom.utils.validate_parent_line_idx",
			"progresserpnext.custom.sales_invoice.validate",
		],
		"before_save": [
			"progresserpnext.custom.sales_invoice.before_save",
			"progresserpnext.custom.utils.calculate_sales_valuation_and_margin",
		],
	},
	"Delivery Note": {
		"before_validate": [
			"progresserpnext.custom.delivery_note.before_validate",
		],
		"validate": [
			"progresserpnext.custom.utils.validate_parent_line_idx",
			"progresserpnext.custom.delivery_note.validate",
		],
		"before_save": [
			"progresserpnext.custom.delivery_note.before_save",
		],
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"progresserpnext.tasks.all"
# 	],
# 	"daily": [
# 		"progresserpnext.tasks.daily"
# 	],
# 	"hourly": [
# 		"progresserpnext.tasks.hourly"
# 	],
# 	"weekly": [
# 		"progresserpnext.tasks.weekly"
# 	],
# 	"monthly": [
# 		"progresserpnext.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "progresserpnext.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "progresserpnext.event.get_events"
# }

override_whitelisted_methods = {
	"erpnext.setup.doctype.transaction_deletion_record.transaction_deletion_record.get_doctypes_to_be_ignored": "progresserpnext.custom.transaction_deletion_record.get_doctypes_to_be_ignored"
}

#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "progresserpnext.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["progresserpnext.utils.before_request"]
# after_request = ["progresserpnext.utils.after_request"]

# Job Events
# ----------
# before_job = ["progresserpnext.utils.before_job"]
# after_job = ["progresserpnext.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"progresserpnext.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# data to be ignored when deleting company transactions
company_data_to_be_ignored = ["Shipping Rule", "Department"]
