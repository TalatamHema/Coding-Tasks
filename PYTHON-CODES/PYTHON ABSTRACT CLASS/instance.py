from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class ChildClass(AbstractClass):
    def abstract_method(self):
        print("Implemented Abstract Method in ChildClass")

    def call_abstract(self):
        obj = ChildClass()
        obj.abstract_method()

# Creating an instance of ChildClass and calling the abstract method
child_obj = ChildClass()
child_obj.call_abstract()
