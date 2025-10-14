import frappe

@frappe.whitelist(allow_guest=True)
def get_member_count():
    """Public API to get member count"""
    return {
        "count": frappe.db.count("Library Member")
    }

@frappe.whitelist()
def create_member(first_name, last_name, email, phone=None):
    """API to create a new member"""
    doc = frappe.get_doc({
        "doctype": "Library Member",
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone
    })
    doc.insert()
    return doc