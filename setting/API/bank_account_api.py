import frappe
from frappe import _
import requests
import json
from frappe.model.document import Document
from frappe.utils import get_site_name



@frappe.whitelist(allow_guest=True)
def get_bank_account_details(**kwargs):
    try:
        name = kwargs.get('name')
        ifsc = kwargs.get('ifsc')
        setting = frappe.get_doc('Setting')
        
        url = setting.sandbox_app_url
        url += "/api/method/sandbox.API.bank_account_api.get_bank_account_details"

        payload={
            'ifsc': ifsc,
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
        print(json_message)
        
        if (json_message['status'] == 'failure'):
            return({'status' : 'failure', 'message' : json_message})
        else:
            store_details(json_message['data'],json_message,name)
            return({'status' : 'success'})
    except Exception as e:
        frappe.logger('Setting').exception(e)

 
def store_details(message,json_message,name):
    ifsc = json_message['ifsc']
    try:
        response = (message['MICR'] +'\n'+ message['BRANCH'] +'\n'+ message['ADDRESS'] +'\n'+ message['STATE'] +'\n'+ message['CITY'] +'\n'+ message['CENTRE'] +'\n'+ message['DISTRICT'] +'\n'+ message['ISO3166'] +'\n'+ message['BANK'] +'\n'+ message['BANKCODE'] +'\n'+ message['CONTACT'])
        doc = frappe.get_doc("Bank Account",name)
        doc.ifsc = ifsc
        doc.fetch_information = response
        doc.save()
        # doc.refresh()
    except Exception as e:
        frappe.logger('Final_Log').exception(e)





