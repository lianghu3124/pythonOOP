# Python Object-Oriented Programming

# Take aways:
"""
1. instance variable:  you can give a instance a new variable outside the class definition anytime you want,
this variable will only belong to that instance
eg:
class Employee:
    pass

emp1 = Employee()
emp1.name = 'Hugh'
2. class variable
"""


class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)  # self.raise_amount also works


emp_1 = Employee('hugh', 'liang', 90000)
emp_2 = Employee('hugh', 'liang', 90000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.raise_amount = 1.06  # This will create an instance variable for this instance;
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__) # namespace of an instance

print(Employee.num_of_emps)



