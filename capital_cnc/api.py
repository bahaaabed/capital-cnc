import frappe

@frappe.whitelist()
def test(doc,methode):
    print(doc.name)
    # frappe.msgprint("TESSSSSSSSSSSS")