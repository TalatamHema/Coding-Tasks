class Parent:
    def __init__(self):
        self.public_field = "Public Field"

    def public_method(self):
        print("Public Method in Parent")

class Child(Parent):
    def access_public(self):
        print(self.public_field)
        self.public_method()

class Other:
    def access_public(self):
        obj = Parent()
        print(obj.public_field)
        obj.public_method()
        
parent_obj = Parent()
print(parent_obj.public_field)
parent_obj.public_method()

child_obj = Child()
child_obj.access_public()

other_obj = Other()
other_obj.access_public()
