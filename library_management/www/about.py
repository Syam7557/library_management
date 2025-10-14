import frappe

def get_context(context):
    context.member_count = frappe.db.count("Library Member")
    return context