class Parent:
    def __init__(self):
        self._protected_field = "Protected Field"

    def _protected_method(self):
        print("Protected Method in Parent")

class Child(Parent):
    def access_protected(self):
        print(self._protected_field)
        self._protected_method()

class Other:
    def access_protected(self):
        obj = Parent()
        print(obj._protected_field)  
        obj._protected_method()  

# Main method
parent_obj = Parent()
print(parent_obj._protected_field)
parent_obj._protected_method()

child_obj = Child()
child_obj.access_protected()

other_obj = Other()
other_obj.access_protected()
