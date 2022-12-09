import frappe
from frappe import _
import requests
from urllib import response
@frappe.whitelist(allow_guest=True)
def get_access_token(**kwargs):
    
    url = "https://api.sandbox.co.in/authenticate"

    headers = {
        'x-api-key': 'key_live_oOCm2VyW4iy4HS3mdJHNEfvydFEBqGZb',
        'x-api-secret': 'secret_live_NgfgPzic95sEho5M3d04OKa0NXnleok7',
        'x-api-version': '1.0.0'
        }
    response = requests.request("POST", url, headers=headers)
    data = response.json()
    return data




@frappe.whitelist(allow_guest=True)
def get_ifsc_verfication(**kwargs):
    ifsc = kwargs.get("ifsc")


    
    data1 = get_access_token()
    

    auth = data1['access_token']
  
    base_url = "https://api.sandbox.co.in/bank/"
    headers = {
        "accept": "application/json",
        "Authorization": auth,
        "x-api-version": "1.0.0"
        }
    url=f"{base_url}{ifsc}"
    # print(url)
    
    response = requests.get(url, headers=headers)
  
    # print(response)
    data = response.json()
    # print(data)
    return data


   










