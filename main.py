from employee import Employee
from employee_manager import EmployeeManager

manager = EmployeeManager()
manager.load_from_csv()

while True:

    print()
    print("========== Employee Management System ==========")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Delete Employee")
    print("4. Update Salary")
    print("5. Update performance score")
    print("6. Update Attendance")
    print("7. Display all employees")
    print("8. Exit")
    print("===============================================")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print()

        name = input("Enter name: ")
        department = input("Enter department: ")
        salary = int(input("Enter salary: "))
        performance_score = int(input("Enter performance score: "))
        attendance = int(input("Enter attendance: "))

        employee_id = manager.generate_employee_id()

        emp = Employee(employee_id, name, department, salary, performance_score, attendance)
        manager.add_employee(emp)
        manager.save_to_csv()

        print()
        print("Employee added")
        print()

    elif choice == 2:
        print()

        employee_id = int(input("Enter employee id: "))
        result = manager.search_employee(employee_id)

        print()

        if result is not None:
            result.display_info()
        else:
            print("Employee doesn't exist")

        print()

    elif choice == 3:
        print()

        employee_id = int(input("Enter employee id: "))
        result = manager.delete_employee(employee_id)

        print()

        if result:
            manager.save_to_csv()
            print("Employee deleted")
        else:
            print("Employee not found")

        print()

    elif choice == 4:
        while True:
            try:
                print()

                employee_id = int(input("Enter employee id: "))
                new_salary = int(input("Enter new salary: "))

                result = manager.update_salary(employee_id, new_salary)

                print()

                if result:
                    manager.save_to_csv()
                    print("Salary updated successfully")
                else:
                    print("Employee not found")

                print()

                break  # so while true cancels out and it get out of loop after output so user can see main dashboard

            except ValueError as e:
                print(e)
                print("Please enter a valid employee id and salary")
                print()

    elif choice == 5:
        while True:
            try:
                print()

                employee_id = int(input("Enter employee id: "))
                new_performance = int(input("Enter new performance score: "))

                result = manager.update_performance(employee_id, new_performance)

                print()

                if result:
                    manager.save_to_csv()
                    print("Performance updated successfully")
                else:
                    print("Employee not found")

                print()

                break

            except ValueError as e:
                print(e)
                print("Please enter a valid employee id and new performance")
                print()

    elif choice == 6:
        while True:
            try:
                print()

                employee_id = int(input("Enter employee id: "))
                new_attendance = int(input("Enter new attendance between 0 to 100: "))

                result = manager.update_attendance(employee_id, new_attendance)

                print()

                if result:
                    manager.save_to_csv()
                    print("Attendance updated successfully")
                else:
                    print("Employee not found")

                print()

                break

            except ValueError as e:
                print(e)
                print("Please enter a valid employee id and new attendance")
                print()

    elif choice == 7:
        print()
        print("========== All Employees ==========")

        manager.display_all_employee()

        print("===================================")
        print()

    elif choice == 8:
        print()
        print("Thank you for using Employee Management System.")
        break

    else:
        print()
        print("Invalid choice")
        print()

            
    
