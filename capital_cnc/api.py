import io
import os
import frappe
from pyqrcode import create as qrcreate

@frappe.whitelist()
def qrcode(doc,methode):
    file_output_name = doc.name

    doctype = "Customer"
    docname = doc.name
    filename = 'QRCode_{}.png'.format(docname).replace(os.path.sep, "__")
    qr_image = io.BytesIO()
    url = qrcreate(f'http://0.0.0.0:8004/buy/buy/{file_output_name}', error='L')
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