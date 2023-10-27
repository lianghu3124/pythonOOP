# Python Object-Oriented Programming
"""
A decorator allows us to define a method, but we can access it like an attribute
getter:  get access to a property
"""


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@gmail.com'

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None


emp_1 = Employee('Corey', 'Schafer')
emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)

emp_1.fullname = 'Hugh Liang'

print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)

del emp_1.fullname

print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)
