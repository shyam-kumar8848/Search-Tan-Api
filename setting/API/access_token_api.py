# import frappe
# from frappe import _
# import requests
# from urllib import response

# @frappe.whitelist(allow_guest=True)
# def get_access_token():
#     setting = frappe.get_doc('Sandbox Setting')
#     url = setting.sandbox_auth_url
#     url = "https://api.sandbox.co.in/authenticate"
#     headers = {
#         "accept": "application/json",                     
#         "x-api-key":setting.x_api_key,
#         "x-api-secret":setting.x_api_secret,
#         "x-api-version":setting.x_api_version
#         }
#     response = requests.request("POST",url, headers=headers)
#     print(response)
#     data = response.json()
#     return data



# @frappe.whitelist(allow_guest=True)
# def get_Employee_details(**kwargs):
#     pan = kwargs.get('pan')
#     adhar = kwargs.get('adhar')
#     data1 = get_access_token()
  
#     auth = data1["access_token"]
#     setting = frappe.get_doc('Sandbox Setting')
#     url = setting.mapping_url
#     # base_url = "https://api.sandbox.co.in/pans/"
#     headers = {
#         "accept": "application/json",
#         "Authorization": auth,
#         "x-api-key":setting.x_api_key,
#         "x-api-version":setting.x_api_version
#         }
#     url=f"{url}{pan}/pan-aadhaar-status?aadhaar_number={adhar}"    
#     # url=f"{url}{pan}"
#     response = requests.request("GET",url, headers=headers)
#     print(response)
#     data = response.json()
#     return data
    




