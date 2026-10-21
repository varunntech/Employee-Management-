from employee import Employee
import pandas as pd

class EmployeeManager:
    def __init__(self):
        self.employees = []
        self.next_id = 1

    def generate_employee_id(self):
        employee_id = self.next_id
        self.next_id += 1
        return employee_id

    def add_employee(self, employee):
        if isinstance(employee, Employee):  # isinstance :-it checks employee is obj of class Employee or not just a easy functionnnn
            self.employees.append(employee)
        else:
            print("Invalid employee object")

    def search_employee(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp

        return None

    def delete_employee(self, employee_id):
        obj = self.search_employee(employee_id)
        if obj is not None:
            self.employees.remove(obj)
            return True
        else:
            return False

    def update_salary(self, employee_id, new_salary):
        if new_salary <= 0:
            raise ValueError("Salary cannot be negative or zero")

        obj = self.search_employee(employee_id)
        if obj is not None:
            obj.salary = new_salary
            return True
        else:
            return False

    def update_performance(self, employee_id, new_performance):
        if new_performance < 0 or new_performance > 100:
            raise ValueError("Performance score must be between 0 and 100")

        obj = self.search_employee(employee_id)
        if obj is not None:
            obj.performance_score = new_performance
            return True
        else:
            return False

    def update_attendance(self, employee_id, new_attendance):
        if new_attendance < 0 or new_attendance > 100:
            raise ValueError("Attendance must be between 0 and 100")

        obj = self.search_employee(employee_id)
        if obj is not None:
            obj.attendance = new_attendance
            return True

        return False

    def display_all_employee(self):
        if not self.employees:  # or if len(self.employees) == 0
            print("No employee found")
        else:
            for emp in self.employees:
                emp.display_info()
            return True

        return False

    # Each employee becomes one dictionary, and all those dictionaries are stored in a list. Then we create one Pandas DataFrame from that list.
    # Algorithm
    # Create an empty list.
    # Loop through self.employees.
    # For each employee, create one dictionary.
    # Append that dictionary to the list.
    # After the loop, create a Pandas DataFrame from the list.
    # Return the DataFrame.

    def convert_to_dataframe(self):
        employee_data = []

        for emp in self.employees:
            employee_dict = {
                "Employee ID": emp.employee_id,
                "Name": emp.name,
                "Department": emp.department,
                "Salary": emp.salary,
                "Performance score": emp.performance_score,
                "Attendance": emp.attendance
            }

            employee_data.append(employee_dict)

        df = pd.DataFrame(employee_data)
        return df

    def get_total_employee(self):
        count = 0

        for i in self.employees:
            count += 1

        return count

    def average_salary(self):  
        total_salary = 0

        if not self.employees:
            print("No employee found")
            return 0
        else:
            for emp in self.employees:
                total_salary += emp.salary

            total_employee = self.get_total_employee()
            average_salary = total_salary / total_employee
            return average_salary

    def highest_salary(self):
        if not self.employees:
            return None

        highest_employee = self.employees[0]

        for emp in self.employees:
            if emp.salary > highest_employee.salary:
                highest_employee = emp

        return highest_employee

    def lowest_salary(self):
        if not self.employees:
            return None

        lowest_employee = self.employees[0]

        for emp in self.employees:
            if emp.salary < lowest_employee.salary:
                lowest_employee = emp

        return lowest_employee

    def highest_performance(self):
        if not self.employees:
            return None

        highest_performance = self.employees[0]

        for emp in self.employees:
            if emp.performance_score > highest_performance.performance_score:
                highest_performance = emp

        return highest_performance

    def employees_below_attendance(self, threshold):
        low_attendance = []

        for emp in self.employees:
            if emp.attendance < threshold:
                low_attendance.append(emp)

        return low_attendance

    def salary_above_threshold(self, threshold):
        salary_above = []

        for emp in self.employees:
            if emp.salary > threshold:
                salary_above.append(emp)

        return salary_above

    def high_performance_employees(self, score):
        high_performance = []

        for emp in self.employees:
            if emp.performance_score > score:
                high_performance.append(emp)

        return high_performance

    def employees_by_department(self):
        department_dict = {}

        for emp in self.employees:
            if emp.department not in department_dict:
                department_dict[emp.department] = []

            department_dict[emp.department].append(emp)

        return department_dict

    def save_to_csv(self):
        df = self.convert_to_dataframe()
        df.to_csv("employees.csv", index=False)

    def load_from_csv(self):
        try:
            df = pd.read_csv("employees.csv")

            self.employees.clear()

            for _, row in df.iterrows():
                emp = Employee(
                    row["Employee ID"],
                    row["Name"],
                    row["Department"],
                    row["Salary"],
                    row["Performance score"],
                    row["Attendance"]
                )

                self.employees.append(emp)

            if not df.empty:
                self.next_id = int(df["Employee ID"].max()) + 1
            else:
                self.next_id = 1

        except FileNotFoundError:
            print("employees.csv not found, starting with an empty employee list.")