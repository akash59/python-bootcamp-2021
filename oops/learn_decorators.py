class Employee:
    """
    Learning OOPS concepts in python
    """
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = self.first + '.' + self.last + '@email.com'

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter
    def fullname(self, f_name):
        first, last = f_name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None

    @property
    def email(self):
        return self.first + '.' + self.last + '@email.com'


emp_1 = Employee('Akash', 'Sood')
emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = 'Corey Schafer'
print(emp_1.fullname)
print(emp_1.first)
print(emp_1.last)

del emp_1.fullname
# print(emp_1.fullname)
print(emp_1.first)
print(emp_1.last)