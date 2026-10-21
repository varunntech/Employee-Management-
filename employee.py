class Employee:
    def __init__(self, employee_id, name, department, salary, performance_score, attendance):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.performance_score = performance_score
        self.attendance = attendance

    def display_info(self):
        print("Emp id: ", self.employee_id)
        print("Name : ", self.name)
        print("Department : ", self.department)
        print("Salary : ", self.salary)
        print("Performance score : ", self.performance_score)
        print("Attendance : ", self.attendance)
