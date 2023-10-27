# Python Object-Oriented Programming
"""
Special/magic/Dunder methods,
dunder means double under, cause they always start with __
Those methods allow us to emulate some build-in behavior within python,
and it's also how we implement operator overloading

"""


class Employee:
    raise_amt = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)  # self.raise_amount also works

    def __repr__(self):
        return "Employee('{}', '{}', '{}' )".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # https://docs.python.org/3/reference/datamodel.html?highlight=numeric%20type#object.__add__
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 90000)
emp_2 = Employee('Hugh', 'Liang', 110000)
print(emp_1)  # without reload __repr__, result would be: <__main__.Employee object at 0x000002B45B812DD0>
print(repr(emp_1))
print(str(emp_1))

print(emp_1+emp_2)
print(len(emp_1))



