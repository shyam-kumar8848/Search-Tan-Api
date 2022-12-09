frappe.ui.form.on('IFSC Verfication', {
    ifsc_verfication:function(frm) {
        frappe.call({
            method: "setting.API.ifsc_verfication_api.get_ifsc_verfication",
            args: {
                ifsc:frm.doc.ifsc

            },
            callback: function (r) {
                let ifsc = r.message;
    
                    frm.set_value("branch",ifsc["BRANCH"])
                    frm.set_value("micr",ifsc["MICR"])
                    frm.set_value("address",ifsc["ADDRESS"])
                    frm.set_value("state",ifsc["STATE"])
                    frm.set_value("contact",ifsc["CONTACT"])
                    frm.set_value("upi",ifsc["UPI"])
                    frm.set_value("rtgs",ifsc["RTGS"])
                    frm.set_value("city",ifsc["CITY"])
                    frm.set_value("centre",ifsc["CENTRE"])
                    frm.set_value("district",ifsc["DISTRICT"])
                    frm.set_value("neft",ifsc["NEFT"])
                    frm.set_value("imps",ifsc["IMPS"])
                    frm.set_value("swift",ifsc["SWIFT"])
                    frm.set_value("country_code",ifsc["ISO3166"])
                    frm.set_value("bank",ifsc["BANK"])
                    frm.set_value("bankcode",ifsc["BANKCODE"])
                    
                    console.log[r.message]
            }
            
            

        });
    }

});
