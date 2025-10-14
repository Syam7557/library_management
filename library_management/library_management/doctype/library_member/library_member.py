import frappe
from frappe.model.document import Document

class LibraryMember(Document):
    def before_save(self):
        # If membership_date is empty, set it to today's date
        if not self.membership_date:
            self.membership_date = frappe.utils.today()

    def validate(self):
        # Normalize email (optional but recommended)
        if getattr(self, "email", None):
            self.email = self.email.strip().lower()

            # Check for duplicate email: use list-of-lists filters for !=
            exists = frappe.db.exists(
                "Library Member",
                [
                    ["Library Member", "email", "=", self.email],
                    ["Library Member", "name", "!=", self.name or ""]
                ],
            )
            if exists:
                frappe.throw(f"Member with email {self.email} already exists")

    @frappe.whitelist()
    def send_welcome_email(self):
        """Send welcome email to member"""
        if not getattr(self, "email", None):
            frappe.throw("No email found for this member")

        frappe.sendmail(
            recipients=[self.email],
            subject="Welcome to Library",
            message=f"Dear {self.first_name or ''},<br>Welcome to our library!",
        )
        frappe.msgprint("Welcome email sent!")
