import frappe
@frappe.whitelist(allow_guest=True)
def get_all_Setting():
    Setting = frappe.db.sql("""SELECT api_key,api_secret FROM `tabSetting`;""" ,as_dict=True)

    return Setting