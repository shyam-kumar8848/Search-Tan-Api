import frappe
from frappe import _
import requests
import json
from frappe.model.document import Document
from frappe.utils import get_site_name

@frappe.whitelist(allow_guest=True)
def get_employee_details(**kwargs):
    try:
        name = kwargs.get('name')
        pan = kwargs.get('pan')
        adhar = kwargs.get('adhar')
        setting = frappe.get_doc('Setting')
        
        url = setting.sandbox_app_url
        url += "/api/method/sandbox.API.employee_details_api.get_employee_details"

        payload={
            'pan': pan,
            'adhar':adhar,
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
            store_details(json_message,name)
            return({'status' : 'success'})
    except Exception as e:
        frappe.logger('Setting').exception(e)

 


def store_details(json_message, name):
    print(json_message)
    res = json_message['data']['message']
    try:
        print("Last Response of Wrapper App",res)
        doc = frappe.get_doc("Employee", name)
        doc.pan_and_aadhar_mapping_status = res
        doc.save()
        print('Employee record saved')
    except Exception as e:
        frappe.logger('Final_Log').exception(e)

