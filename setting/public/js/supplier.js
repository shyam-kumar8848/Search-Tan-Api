frappe.ui.form.on('Supplier', {
    fetch_tan_no:function(frm) {
        frappe.call({
                    method: "setting.API.supplier_api.get_supplier_details",
                    args: {
                        tan_no:frm.doc.tan_no,
                        name: frm.doc.name
                    },
                    callback: function (r) {
                      
                    
                        console.log[r.data]
                    }
                });
        
    
    }

});
