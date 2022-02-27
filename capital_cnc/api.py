import io
import os
import frappe
from pyqrcode import create as qrcreate
from frappe.utils.background_jobs import enqueue

@frappe.whitelist()
def qrcode(doc,methode):
    file_output_name = doc.name
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

# def send_email(self, recipients ,sender= None, msg = 'tset', subject= 'test'):
#         """send email with payment link"""
#         email_args = {
#             "recipients": self.email_to,
#             "sender": None,
#             "subject": self.subject,
#             "message": self.get_message(),
#             "now": True,
#             "attachments": [frappe.attach_print(self.reference_doctype, self.reference_name,
#                 file_name=self.reference_name, print_format=self.print_format)]}
#         enqueue(method=frappe.sendmail, queue='short', timeout=300, is_async=True, **email_args)


