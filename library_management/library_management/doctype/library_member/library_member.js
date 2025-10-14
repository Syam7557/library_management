
frappe.ui.form.on('Library Member', {
    refresh: function(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button('Send Welcome Email', function() {
                frm.call('send_welcome_email').then(() => {
                    frappe.show_alert({
                        message: 'Email Sent',
                        indicator: 'green'
                    });
                });
            });
        }
    }
});