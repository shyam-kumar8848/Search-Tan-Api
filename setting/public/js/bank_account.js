frappe.ui.form.on('Bank Account', {
    ifsc_verfication:function(frm) {
        frappe.call({
            method: "setting.API.bank_account_api.get_bank_account_details",
            args: {
                ifsc:frm.doc.ifsc,
                name:frm.doc.name

            },
            callback: function (r) {
                    
                    console.log[r.message]
            }
            
            

        });
    }

});
