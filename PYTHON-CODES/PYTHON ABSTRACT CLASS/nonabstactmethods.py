from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        print("Non-Abstract Method in AbstractClass")

class ChildClass(AbstractClass):
    def abstract_method(self):
        print("Implemented Abstract Method in ChildClass")

    def call_non_abstract(self):
        obj = ChildClass()
        obj.non_abstract_method()

# Creating an instance of ChildClass and calling the non-abstract method
child_obj = ChildClass()
child_obj.call_non_abstract()
