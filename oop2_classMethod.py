# Python Object-Oriented Programming

# Take aways:
"""
1. regular methods, class methods and static methods
2. use class methods as alternative constructors
    real life example: C:\\Users\\nliang\\AppData\\Local\\anaconda3\\Lib\\datetime.py line 958
    @classmethod
    def fromtimestamp(cls, t):
        "Construct a date from a POSIX timestamp (like time.time())."
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
        return cls(y, m, d)

    @classmethod
    def today(cls):
        "Construct a date from time.time()."
        t = _time.time()
        return cls.fromtimestamp(t)
3. static methods have no self or cls
    we include them because they have some logical connection with the class
    if you don't access the instance or the class anywhere within the function

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

    @classmethod  # this is called a decorator
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod  # this is called: use class methods as alternative constructors
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return Employee(first, last, pay)  # same as cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True




emp_1 = Employee('Corey', 'Schafer', 90000)
emp_2 = Employee('hugh', 'liang', 90000)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)


emp_str_1 = 'Hugh-Liang-80000'
emp_str_2 = 'Dave-Meyer-288888'
emp_str_3 = 'John-Doe-90000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)


new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.email)
print(new_emp_2.last)


import datetime
my_date = datetime.date(2023, 12, 25)
print(Employee.is_workday(my_date))