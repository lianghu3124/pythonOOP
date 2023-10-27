# Python Object-Oriented Programming
"""
Inheritance
Takeaways:
1. don't pass [], because you never want to pass mutable data like a list or dictionary as default arg
2. isinstance  issubclass
3. real life inheritance example:  C:\\Users\\nliang\\AppData\\Local\anaconda3\\Lib\\site-packages\\werkzeug\\exception.py line 174

    ""*400* `Bad Request`

    Raise if the browser sends something to the application the application
    or server cannot handle.
    "" "

    code = 400
    description = (
        "The browser (or proxy) sent a request that this server could "
        "not understand."
    )
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


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # prefer this when it's single inheritance
        # Employee.__init__(self, first, last, pay)  # this works better when it's multiple inheritance
        self.prog_lang = prog_lang


class Manager(Employee):

    # don't pass [], because you never want to pass mutable data like a list or dictionary as default arg
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 110000, 'python')
dev_2 = Developer('hugh', 'liang', 90000, 'Java')

print(dev_1.email, dev_1.prog_lang)
print(dev_2.email)

# print(help(Developer))

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print(issubclass(Developer, Employee))

