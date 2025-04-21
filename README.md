# Employee_Management_Frappe
a Frappe application to manage employee records 

1) For User Sign-Up and Sign-In:
I used the Frappe's built-in user authentication and ensured sign-up is enabled by modifying hooks.py
Then created a login page using Frappe's authentication system.

2) Doctypes
I created the first Doctype Employee with the following Fields
    Full Name (Data)
    Email Address (Data)
    Phone Number (Data)
    Position (Select: Manager, Developer, Designer, etc.)
    Date of Joining (Date)
   
3) For Logging I created another Doctype
"Employee Log" with the following fields

    Type of Operation (Data) - operation_type
    User (Link) - user (Link to "User")
    Timestamp (Datetime) - timestamp (Default: frappe.utils.now())
    Employee (Link) - employee (Link to "Employee")
    Details (Long Text) - details (Optional for change diffs)

Dashboard showing number of Employees
![image](https://github.com/user-attachments/assets/fba5b23c-4050-4036-9b74-48492152fb5c)

Filtering by Positions
![image](https://github.com/user-attachments/assets/317d4f69-d6f6-4752-a492-88fcb4d7bae9)

