frappe.ui.form.on('Employee', {
    refresh: function (frm) {
        
        frappe.model.with_doc("Setting", frm.doc.trigger, function () {
            var emp = frappe.model.get_doc("Setting")
            if (emp.pan_and_aadhar_mapping_status == 1) {
                frm.add_custom_button(('status'), function () {
                    frappe.call({
                        method: "setting.API.employee_details_api.get_employee_details",
                        args: {
                            pan: frm.selected_doc.pan_card_no,
                            adhar: frm.selected_doc.aadhaar_card_no,
                            name: frm.doc.name
                        },
                        callback: function (r) {
                            if (r.message) {

                                let mapping_status = r.message.data['message'];
                                if (frm.doc.pan_card_no && frm.doc.aadhaar_card_no) {
                                    frm.set_value('pan_and_aadhar_mapping_status', mapping_status)
                                }
                                else {
                                    frm.set_value('pan_and_aadhar_mapping_status', " ")
                                }
                                if (frm.doc.pan_card_no) {
                                    if (frm.doc.aadhaar_card_no == "") {
                                        frm.set_value('pan_and_aadhar_mapping_status', "Enter Aadhar Card Details.")
                                    }
                                    if (frm.doc.aadhaar_card_no) {
                                        if (frm.doc.pan_card_no == "") {
                                            frm.set_value('pan_and_aadhar_mapping_status', "Enter PAN Card Details.")
                                        }
                                    }
                                    // alert(r.message['status']);
                                }
                            }

                        }
                    });

                })

            }
        })
    }
})














