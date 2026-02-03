import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="payroll")

cursor = conn.cursor()

def show_employees():
    cursor.execute("""
        SELECT e.emp_id, e.name, d.dept_name, e.base_salary,
               (e.base_salary + IFNULL(p.bonus,0) - IFNULL(p.deductions,0)) AS net_salary
        FROM employees e
        LEFT JOIN departments d ON e.dept_id = d.dept_id
        LEFT JOIN payroll p ON e.emp_id = p.emp_id
    """)
    for row in cursor.fetchall():
        print(row)

def update_salary():
    emp_id = int(input("Employee ID: "))
    salary = float(input("New base salary: "))
    cursor.execute(
        "UPDATE employees SET base_salary=%s WHERE emp_id=%s",
        (salary, emp_id)
)
    conn.commit()

def delete_employee():
    emp_id = int(input("Employee ID to delete: "))
    cursor.execute("DELETE FROM payroll WHERE emp_id=%s", (emp_id,))
    cursor.execute("DELETE FROM employees WHERE emp_id=%s", (emp_id,))
    conn.commit()

def add_employee():
    cursor.execute("")
    conn.commit()

while True:
    print("\n1. Show Employees")
    print("2. Update Salary")
    print("3. Delete Employee")
    print("4. Add employee")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        show_employees()
    elif choice == "2":
        update_salary()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        add_employee()
    elif choice == "5":
        break
    else:
        print("Invalid option")
