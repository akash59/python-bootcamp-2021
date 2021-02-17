def add_numbers(*args):
    return sum(args)


class Employee:
    """
    Learning OOPS concepts in python
    """
    raise_amount = 1.04
    no_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.no_of_employees += 1

    def __str__(self):
        return f'{self.first} - {self.last} - {self.pay}'

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        else:
            return NotImplemented

    def __len__(self):
        return len(self.fullname())

    @classmethod
    def get_employee(cls, first, last):
        return cls(first, last, "")

    def fullname(self):
        print(f'My full name is - {self.first}, {self.last}')
        return self.first + ' ' + self.last

    def apply_raise(self):
        # raise_amount : can be accessed using self (when you want to change value per instance) or by className (
        # preferred when want to create constant)
        self.pay = int(self.pay * self.raise_amount)

    def get_pay(self):
        print(f'my salary is {self.pay}')
        return self.pay

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def validate_name_length(name):
        return len(name) <= 10


class Developer(Employee):
    raise_amount = 1.15

    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        self.language = language

    def __str__(self):
        return f'{self.first} - {self.last} - {self.pay} - {self.language}'

    def __repr__(self):
        return "Employee('{}', '{}', {}, '{}')".format(self.first, self.last, self.pay, self.language)


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            employee.fullname()


e1 = Employee('Test', 'Employee', 195000)
print(e1)
print(str(e1))

dev_1 = Developer('Akash', 'Sood', 100000, 'Python')
dev_2 = Developer('Jack', 'Martin', 1000, 'Java')
Employee.set_raise_amount(1.05)
print(dev_1)
print(repr(dev_1))

print(dev_1 + dev_2)
print('Dev 2 name length {}'.format(len(dev_2)))


manager_1 = Manager('Sue', 'Smith', 213123, [dev_1])
print(manager_1.first)
manager_1.print_employees()
manager_1.add_employee(dev_2)
manager_1.print_employees()
manager_1.remove_employee(dev_1)
manager_1.print_employees()

print(isinstance(manager_1, Manager))
print(isinstance(manager_1, Employee))
print(isinstance(manager_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Manager))


print(Employee.raise_amount)
dev_1.apply_raise()
print(dev_1.get_pay())
print(dev_1.language)

print(dev_2.raise_amount)
print(dev_2.get_pay())
print(dev_2.language)

#
# emp_3 = Employee.get_employee('Test', 'Employee')
# print(emp_3.first)
# print(emp_3.last)
# print(emp_3.raise_amount)
# emp_3.raise_amount = 1.07
# print(emp_3.__dict__)
# print(emp_3.raise_amount)
# print(Employee.raise_amount)
# print(dev_2.raise_amount)

print(help(Developer))
