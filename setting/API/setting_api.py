import frappe
from frappe import _
import requests
from frappe.model.document import Document
# from setting.API.setting_api import access_token
from urllib import response

@frappe.whitelist(allow_guest=True)
def get_access_token():
    setting = frappe.get_doc('Setting')
    url = setting.sandbox_auth_url

    url+= "/api/method/setting.setting.API.setting_api.get_Employee_details"
    url = "https://api.sandbox.co.in/authenticate"
    headers = {
        "accept": "application/json",                     
        "x-api-key":setting.api_key,
        "x-api-secret":setting.api_secret,
        # "x-api-version":setting.x_api_version
        }

        
    response = requests.request("POST",url, headers=headers)
    print(response)
    data = response.json()
    
    return data


@frappe.whitelist(allow_guest=True)
def get_Employee_details(**kwargs):
    pan = kwargs.get('pan')
    adhar = kwargs.get('adhar')
    data1 = get_access_token()
    auth = data1["access_token"]
    setting = frappe.get_doc('Setting')
    url = setting.api_key
    url = setting.api_secret
    base_url = "https://api.sandbox.co.in/pans/"
    headers = {
        "accept": "application/json",
        "Authorization": auth,
        "x-api-key":setting.api_key,
        "x-api-version":setting.x_api_version
        }


    st = frappe.get_doc('Setting', kwargs.get('doc'))
    status = frappe.get_value('Address', st.billing_address,'gstin')
    data = json.loads(kwargs.get('data'))
    data = {
        "ewbNo": sc.ewaybill,
        "cancelRsnCode":data.get('reason'),
        "cancelRmrk" : data.get('remarks'),
        "gstin":status
        }
    url=f"{url}{pan}/pan-aadhaar-status?aadhaar_number={adhar}"    
    # url=f"{url}{pan}"
    response = requests.request("GET",url, headers=headers)
    print(response)
    data = response.json()
    return data
    
