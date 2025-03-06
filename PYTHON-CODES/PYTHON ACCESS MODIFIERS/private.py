class Parent:
    __private_field = "Private Field"

    def __private_method(self):
        print("Private Method in Parent")

    def access_private(self):
        print(self.__private_field)
        self.__private_method()

class Child(Parent):
    def try_access_private(self):
        print("Cannot access private members from Child class")


parent_obj = Parent()
parent_obj.access_private()

child_obj = Child()
child_obj.try_access_private()
