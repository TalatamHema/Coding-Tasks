from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        print("Non-Abstract Method in AbstractClass")

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Implemented Abstract Method in ConcreteClass")

# Main method
obj = ConcreteClass()
obj.abstract_method()
obj.non_abstract_method()
