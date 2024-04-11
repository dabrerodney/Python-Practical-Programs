class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
    
    def display_info(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)

# Example usage:
employee = Employee("John", "HR", 50000)
employee.display_info()
