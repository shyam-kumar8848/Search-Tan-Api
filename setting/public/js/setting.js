frappe.ui.form.on('Employee', {
    refresh:function(frm) {
      frm.add_custom_button(('status'), function(){
        frappe.call({
            method: "setting.API.employee_details_api.get_employee_details",
            args: {
                
                pan:frm.selected_doc.pan_card_no,
                adhar:frm.selected_doc.aadhaar_card_no,
                employee_name: frm.doc.name
            },
            callback: function (r) {
                if (r.message){
                    let mapping_status=r.message.data['message'];
                    if (frm.doc.pan_card_no && frm.doc.aadhaar_card_no) {
                        frm.set_value('pan_and_aadhar_mapping_status',mapping_status )
                    }
                    else{
                        frm.set_value('pan_and_aadhar_mapping_status'," ")
                    }
                    if (frm.doc.pan_card_no){
                        if (frm.doc.aadhaar_card_no =="") {
                            frm.set_value('pan_and_aadhar_mapping_status',"Enter Aadhar Card Details.")
                        }
                    }
                    if (frm.doc.aadhaar_card_no){
                        if (frm.doc.pan_card_no =="") {
                            frm.set_value('pan_and_aadhar_mapping_status',"Enter PAN Card Details.")
                        }
                    }
                }
                // console.log(r.message['status'])
                alert(r.message['status']);
                // //frappe.msgprint("Details stored Successfully!")
            }
        });
    })
    }
})



// frappe.ui.form.on('Supplier', {
//     refresh: function(frm) {
//         frm.add_custom_button(('206AB/CCA Check'), function(){
//             frappe.call({
//                 method: "settings.settings.API.tds_tax_act_api.tds_tax_act",
//                 args: {
//                     'pan': frm.doc.pan,
//                     'supplier_name': frm.doc.supplier_name
//                 },
//                 callback: function (r) {
//                     if (r){
//                         console.log(r.[''])
//                         alert(r['message']['data']);
//                         //frappe.msgprint("Details stored Successfully!")
//                     }
//                     else {
//                         frappe.throw(r.message.error)
//                     }
//                 }
//             });
//         });
//     }
// });









