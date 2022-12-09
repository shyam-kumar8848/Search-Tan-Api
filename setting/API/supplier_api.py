import frappe
from frappe import _
import requests
import json
from frappe.model.document import Document
from frappe.utils import get_site_name
import time
import datetime as dt


@frappe.whitelist(allow_guest=True)
def get_supplier_details(**kwargs):
    try:
        name = kwargs.get('name')
        tan_no = kwargs.get('tan_no')
        setting = frappe.get_doc('Setting')
        
        url = setting.sandbox_app_url
        url += "/api/method/sandbox.API.supplier_api.get_supplier_details"

        payload={
            'tan_no': tan_no,
            'name':name,
            'site_name': get_site_name(frappe.local.request.host)
        }
        headers = {
            'x-api-key': setting.x_api_key,
            'x-api-secret' : setting.x_api_secret
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        json_response = response.json()
        json_message = json_response['message']
      

        if (json_message['status'] == 'failure'):
            return({'status' : 'failure', 'message' : json_message})
        else:
            store_details(json_message['data'],json_message,name)
            return({'status' : 'success'})
    except Exception as e:
        frappe.logger('Setting').exception(e)

 
def store_details(message,json_message,name):
    tan = json_message['tan']
    unix_date=1534251701000
    date=dt.datetime.utcfromtimestamp(unix_date/1000).strftime("%d/%m/%Y %H:%M:%S")
    try:
        nameOrgn = message['nameOrgn']
        addLine1 = (message['addLine2'] +'\n'+ message['addLine4'] +'\n'+ message['addLine5']+'\n'+str(message['pin']))
        doc = frappe.get_doc("Supplier",name)
        doc.tan_no = tan
        doc.nameorgn = nameOrgn
        doc.addline1 = addLine1
        doc.dttanallotment = date
        doc.save()
        doc.refresh()
    except Exception as e:
        frappe.logger('Final_Log').exception(e)



 