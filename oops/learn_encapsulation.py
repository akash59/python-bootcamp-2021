class Base:
    def __init__(self):
        # protected member
        self._a = 2

        # private member
        self.__b = 'private member'

    def __test_private_function(self):
        print("I am a private function..")

    def test_public_function(self):
        print("I am a public function.. i can return private members value")
        print(self.__b)


class Derived(Base):

    def __init__(self):
        Base.__init__(self)
        print('Calling protected member of base class')
        print(self._a)
        print('Calling private member of a base class')
        # print(self.__b) # - this will throw an error
        self.test_public_function()
        # self.__test_private_function() # - can't access private methods outside the class

        # Name mangling
        # self._Base__test_private_function()


obj1 = Base()
print(obj1._a)
# print(obj1.__b) - can't access private member outside the class

obj2 = Derived()  # - can't access private member inside the derived class
# print(obj2._a)


