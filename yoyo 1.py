class DegreeLevel:
    BSc = 0
    MSc = 1
    PhD = 2

class Employee:
    def __init__(self, id, name, department, degree_level, experience, salary):
        self.id = id
        self.name = name
        self.department = department
        self.degree_level = degree_level
        self.experience = experience
        self.salary = salary

def write_employee_to_file(emp, file_path):
    with open(file_path, 'a') as file:
        file.write(f"{emp.id},{emp.name},{emp.department},{emp.degree_level},{emp.experience},{emp.salary}\n")

def read_employees_from_file(file_path):
    employees = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                emp_data = line.strip().split(',')
                emp = Employee(int(emp_data[0]), emp_data[1], emp_data[2], int(emp_data[3]), int(emp_data[4]), float(emp_data[5]))
                employees.append(emp)
    except FileNotFoundError:
        pass
    return employees

def register_employee():
    emp_id = int(input("Enter employee ID: "))
    emp_name = input("Enter employee name: ")
    emp_department = input("Enter employee department: ")

    print("Choose degree level (0 for BSc, 1 for MSc, 2 for PhD): ")
    degree_choice = int(input())
    if degree_choice < 0 or degree_choice > 2:
        print("Invalid degree choice. Defaulting to BSc.")
        degree_level = DegreeLevel.BSc
    else:
        degree_level = degree_choice

    emp_experience = int(input("Enter employee experience (in years): "))

    # Calculate salary based on department, degree level, and experience
    if degree_level == DegreeLevel.BSc:
        emp_salary = 50000 + emp_experience * 2000
    elif degree_level == DegreeLevel.MSc:
        emp_salary = 60000 + emp_experience * 2500
    else:
        emp_salary = 70000 + emp_experience * 3000

    emp = Employee(emp_id, emp_name, emp_department, degree_level, emp_experience, emp_salary)
    write_employee_to_file(emp, "employees.txt")

    print("Employee registered successfully!")

def calculate_salary():
    search_id = int(input("Enter employee ID to calculate salary: "))
    employees = read_employees_from_file("employees.txt")

    found = False
    for emp in employees:
        if emp.id == search_id:
            found = True
            print(f"Salary for employee {emp.name} (ID: {emp.id}) is: {emp.salary}")
            break

    if not found:
        print("Employee not found!")

def search_employee():
    search_id = int(input("Enter employee ID to search: "))
    employees = read_employees_from_file("employees.txt")

    found = False
    for emp in employees:
        if emp.id == search_id:
            found = True
            print("Employee found!")
            print(f"Employee ID: {emp.id}")
            print(f"Employee Name: {emp.name}")
            print(f"Employee Department: {emp.department}")
            print(f"Employee Degree Level: {emp.degree_level}")
            print(f"Employee Experience: {emp.experience} years")
            print(f"Employee Salary: {emp.salary}")
            break

    if not found:
        print("Employee not found!")

def update_employee():
    update_id = int(input("Enter employee ID to update information: "))
    employees = read_employees_from_file("employees.txt")

    found = False
    for i, emp in enumerate(employees):
        if emp.id == update_id:
            found = True
            print(f"Enter new information for employee {emp.name} (ID: {emp.id}):")

            emp.name = input("Update employee name: ")
            emp.department = input("Update employee department: ")

            print("Choose new degree level (0 for BSc, 1 for MSc, 2 for PhD): ")
            degree_choice = int(input())
            if degree_choice < 0 or degree_choice > 2:
                print("Invalid degree choice. Defaulting to BSc.")
                emp.degree_level = DegreeLevel.BSc
            else:
                emp.degree_level = degree_choice

            emp.experience = int(input("Update employee experience (in years): "))

            # Update salary based on updated information
            if emp.degree_level == DegreeLevel.BSc:
                emp.salary = 50000 + emp.experience * 2000
            elif emp.degree_level == DegreeLevel.MSc:
                emp.salary = 60000 + emp.experience * 2500
            else:
                emp.salary = 70000 + emp.experience * 3000

            employees[i] = emp
            print("Employee information updated successfully!")
            break

    if not found:
        print("Employee not found!")

    with open("employees.txt", "w") as file:
        for emp in employees:
            write_employee_to_file(emp, "employees.txt")

def menu():
    choice = None
    while choice != 5:
        print("HARAMAYA UNIVERSITY HRMS")
        print("1. Register Employee")
        print("2. Calculate Salary")
        print("3. Search Employee by ID")
        print("4. Update Employee Information")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            register_employee()
        elif choice == 2:
            calculate_salary()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            update_employee()
        elif choice == 5:
            print("Exiting HRMS...")
        else:
            print("Invalid choice! Please try again.")
        print()

def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if username == "admin" and password == "admin1212":
        print("Admin login successful!")
        menu()
    else:
        print("Invalid admin username or password. Exiting HRMS.")

def main():
    admin_login()

if __name__ == "__main__":
    main()
