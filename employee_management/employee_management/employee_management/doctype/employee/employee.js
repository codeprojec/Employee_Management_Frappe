// Copyright (c) 2025, T Chikumbo and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Employee", {
// 	refresh(frm) {

// 	},
// });

{
    "fields": [
        // Existing fields
        {
            "fieldname": "position",
            "fieldtype": "Link",
            "label": "Position",
            "options": "Position"
        }
    ],
    "list_view": {
        "filters": [
            {
                "fieldname": "employee_name",
                "label": "Name",
                "fieldtype": "Data"
            },
            {
                "fieldname": "position",
                "label": "Position",
                "fieldtype": "Link",
                "options": "Position"
            }
        ]
    }
}