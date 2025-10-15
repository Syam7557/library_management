import frappe
from frappe import _
from frappe.utils import get_url

no_cache = 1
no_sitemap = 1

def get_context(context):
    # Redirect if already logged in
    if frappe.session.user != "Guest":
        frappe.local.flags.redirect_location = get_url("/app")
        raise frappe.Redirect
    
    context.no_cache = 1
    context.no_breadcrumbs = True
    context.title = _("Login")
    context.provider_logins = []
    context.disable_signup = frappe.utils.cint(
        frappe.db.get_single_value("Website Settings", "disable_signup")
    )
    
    return context
