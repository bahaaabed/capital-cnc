import io
import os
import frappe
from pyqrcode import create as qrcreate
from frappe.utils.background_jobs import enqueue

@frappe.whitelist()
def qrcode(doc,methode):
    doctype = "Customer"
    docname = doc.name
    filename = 'QRCode_{}.png'.format(docname).replace(os.path.sep, "__")
    qr_image = io.BytesIO()
    url = qrcreate(f'https://capital-cnc.frappe.cloud/all-products', error='L')
    url.png(qr_image, scale=2, quiet_zone=1)
    _file = frappe.get_doc({
        "doctype": "File",
        "file_name": filename,
        "attached_to_doctype": doctype,
        "attached_to_name": docname,
        "attached_to_field": "qrcode_image",
        "is_private": 0,
        "content": qr_image.getvalue()})
    _file.save()
    frappe.db.commit()
    doc.qr = _file.file_url
    frappe.sendmail(recipients = doc.owner, subject = "Products Page", message = f'https://capital-cnc.frappe.cloud{doc.qr}')

