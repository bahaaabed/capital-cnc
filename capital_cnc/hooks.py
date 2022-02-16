from . import __version__ as app_version

app_name = "capital_cnc"
app_title = "capital"
app_publisher = "capital"
app_description = "capital"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "capita"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/capital_cnc/css/capital_cnc.css"
# app_include_js = "/assets/capital_cnc/js/capital_cnc.js"

# include js, css files in header of web template
# web_include_css = "/assets/capital_cnc/css/capital_cnc.css"
# web_include_js = "/assets/capital_cnc/js/capital_cnc.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "capital_cnc/public/scss/website"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "capital_cnc.install.before_install"
# after_install = "capital_cnc.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "capital_cnc.uninstall.before_uninstall"
# after_uninstall = "capital_cnc.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "capital_cnc.notifications.get_notification_config"

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
# 	"Journal Entry": "capital_cnc.override"
# }

# Document Events
# ---------------
# Hook on document methods and events
doc_events = {
	"Employee": {
		"on_update": "capital_cnc.api.test"
	}
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"capital_cnc.tasks.all"
# 	],
# 	"daily": [
# 		"capital_cnc.tasks.daily"
# 	],
# 	"hourly": [
# 		"capital_cnc.tasks.hourly"
# 	],
# 	"weekly": [
# 		"capital_cnc.tasks.weekly"
# 	]
# 	"monthly": [
# 		"capital_cnc.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "capital_cnc.install.before_tests"

# Overriding Methods
# ------------------------------
#

override_whitelisted_methods = {
	"erpnext.accounts.doctype.journal_entry.journal_entry.get_exchange_rate": "capital_cnc.journal_entry.get_exchange_rate"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "capital_cnc.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"capital_cnc.auth.validate"
# ]

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            ["name", "in", [
				"Journal Entry Account-vlaue",
				"Journal Entry Account-debit_or_credit",
				"Journal Entry Account-select_currancy",
				"Journal Entry Account-exchange_rate_cap",
			]
			]
		]
	}
]