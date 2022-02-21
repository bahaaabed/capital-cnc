# Copyright (c) 2022, capital and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime, timedelta

def execute(filters=None):
	if not filters: filters = {}

	columns = get_columns()
	data = get_entries(filters)
	return columns, data


def get_columns():
	columns = [
		{
			'fieldname': 'journal_entry',
			'label': ('Journal Entry'),
			'fieldtype': 'Link',
			'options': 'Journal Entry',
			"width": 150
		},
		{
			'fieldname': 'account',
			'label': ('Account'),
			'fieldtype': 'Link',
			'options': 'Account',
			"width": 150
		},
		{
			'fieldname': 'account_balance',
			'label': ('Account Balance'),
			'fieldtype': 'Currency',
			'options': 'currency',
			"width": 150
		},
		{
			'fieldname': 'select_currancy',
			'label': ('Currancy'),
			'fieldtype': 'Data',
			'options': 'Data',
			"width": 150
		},
		{
			'fieldname': 'original_amount',
			'label': ('Original Amount'),
			'fieldtype': 'Data',
			'options': 'Data',
			"width": 150
		},
		{
			'fieldname': 'debit_or_credit',
			'label': ('Debit or Credit'),
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'debit_in_account_currency',
			'label': ('Debit'),
			'fieldtype': 'Currency',
			'options': 'currency',
			"width": 150
		},
		{
			'fieldname': 'credit_in_account_currency',
			'label': ('Credit'),
			'fieldtype': 'Currency',
			'options': 'currency',
			"width": 150
		},
		{
			'fieldname': 'party_type',
			'label': ('Party Type'),
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'party',
			'label': ('Party'),
			'fieldtype': 'Data',
			"width": 150
		}
		]
	return columns

def get_entries(filters):
	data = []
	filters['from_date'] = filters.get('from_date')
	filters['to_date'] = filters.get('to_date')
	# conditions = get_conditions(filters)
	journal_entries =  frappe.db.sql("""
	SELECT je.`name` as na,
	jea.account,
	jea.balance,
	jea.select_currancy,
	jea.vlaue,
	jea.debit_or_credit,
	jea.debit_in_account_currency,
	jea.credit_in_account_currency,
	party,
	jea.party_type
	from `tabJournal Entry` je
	LEFT JOIN `tabJournal Entry Account` jea
	on jea.parent = je.name
	where je.creation between '2022-01-01' and '2022-02-20'
	""".format(filters['from_date'],filters['to_date']), filters, as_list=1)
	print(journal_entries)
	return journal_entries
