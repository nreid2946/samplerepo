#Python object oriented programming.
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." +  last + "@company.com"

    def details(self):
        return "Name: {} {} \nSalary: {} \nEmail: {}".format(self.first, self.last, self.pay, self.email)

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Nicholas", "Schafer", 50000)

print(emp_1.details())
print(emp_2.details())
