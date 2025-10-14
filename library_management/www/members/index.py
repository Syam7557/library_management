import frappe

def get_context(context):
    context.members = frappe.get_all(
        "Library Member",
        fields=["name", "first_name", "last_name", "email", "membership_date"],
        order_by="creation desc"
    )
    return context