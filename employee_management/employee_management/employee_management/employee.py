import frappe
from frappe.model.document import Document

class Employee(Document):
    def before_insert(self):
        self.log_operation("Create")

    def on_update(self):
        self.log_operation("Update")

    def on_trash(self):
        self.log_operation("Delete")

    def log_operation(self, operation_type):
        log = frappe.get_doc({
            "doctype": "Employee Log",
            "operation_type": operation_type,
            "user": frappe.session.user,
            "employee": self.name,
            "timestamp": frappe.utils.now(),
            "details": self.get_change_details() if operation_type == "Update" else ""
        })
        log.insert(ignore_permissions=True)
    
    def get_change_details(self):
        old_doc = self.get_doc_before_save()
        if not old_doc:
            return ""
        
        changes = []
        for field in self.meta.fields:
            if self.get(field.fieldname) != old_doc.get(field.fieldname):
                changes.append(f"{field.label}: {old_doc.get(field.fieldname)} → {self.get(field.fieldname)}")
        
        return "\n".join(changes)
    
    from frappe.model.document import Document
import frappe
from frappe.utils import validate_email_address

class Employee(Document):
    def validate(self):
        # Validate email format
        if self.email:
            validate_email_address(self.email, throw=True)
        
        # Add additional validations (e.g., date of birth < today)
        if self.date_of_birth and self.date_of_birth > frappe.utils.today():
            frappe.throw("Date of Birth cannot be in the future")