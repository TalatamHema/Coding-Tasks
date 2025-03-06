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

# Creating an object of ChildClass and accessing non-abstract methods
obj = ChildClass()
obj.non_abstract_method()
