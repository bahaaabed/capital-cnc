import erpnext
from erpnext.accounts.doctype.journal_entry.journal_entry import get_exchange_rate
from frappe.model.document import Document
import frappe
from frappe.utils.data import flt

@frappe.whitelist()
def get_exchange_rate(posting_date, account=None, account_currency=None, company=None,
		reference_type=None, reference_name=None, debit=None, credit=None, exchange_rate=None,select_currancy=None,exchange_rate_cap=None):
    print("********************8888")
    print("********************8888")
    print("********************8888")
	# from erpnext.setup.utils import get_exchange_rate
	# account_details = frappe.db.get_value("Account", account,
	# 	["account_type", "root_type", "account_currency", "company"], as_dict=1)

	# if not account_details:
	# 	frappe.throw(_("Please select correct account"))

	# if not company:
	# 	company = account_details.company

	# if not account_currency:
	# 	account_currency = account_details.account_currency

	# company_currency = erpnext.get_company_currency(company)
	

	# if account_currency != company_currency:
	# 	if reference_type in ("Sales Invoice", "Purchase Invoice") and reference_name:
	# 		exchange_rate = frappe.db.get_value(reference_type, reference_name, "conversion_rate")

	# 	# The date used to retreive the exchange rate here is the date passed
	# 	# in as an argument to this function.
	# 	elif (not exchange_rate or flt(exchange_rate)==1) and account_currency and posting_date:
	# 		exchange_rate = get_exchange_rate(account_currency, company_currency, posting_date)
	# else:
	# 	exchange_rate = 1

	# # don't return None or 0 as it is multipled with a value and that value could be lost
	# return exchange_rate,exchange_rate_cap or 1