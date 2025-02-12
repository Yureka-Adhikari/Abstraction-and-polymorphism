from abc import ABC, abstractmethod

class abstract(ABC):
    
    def print(self, x):
        print(f"The passed value is : {x}")
        
    @abstractmethod
    def task(self):
        print("This is an Abstract method")
        
class test_class(abstract):
    def task(self):
        print("We are inside test_class [But this is not abstract]")
        
        
test_obj = test_class()
test_obj.task()
test_obj.print(100)

