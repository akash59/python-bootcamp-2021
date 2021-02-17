class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} says WOOF!!')


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} says MEOW!!!')


niko = Dog('niko')
niko.speak()
felix = Cat('felix')
felix.speak()

for pet in [niko, felix]:
    print(type(pet))
    pet.speak()


def pet_speak(my_pet):
    my_pet.speak()


pet_speak(niko)
pet_speak(felix)