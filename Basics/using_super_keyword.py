class Animal:
    name = "animal"

    """ 
    Here animal class have variable name with value animal
    Child class that is dog have variable name with value dog
    So usually child class overrides super class so from child class
    If we see the value of name is dog
    To get the value of super class we use 'super' :keyword 
    """

    def __init__(self):
        print("Super class constructor was called")


class Dog(Animal):
    name = "dog"

    def __init__(self):
        print(self.name)  # Prints dog
        print(super().name)  # Prints animal
        super(Dog, self).__init__()  # Super class constructor was called here


def main():
    dog = Dog()


main()
