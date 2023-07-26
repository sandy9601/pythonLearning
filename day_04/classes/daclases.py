age=25



class MyClass:
    """a simple class name"""
    def __init__(self) -> None:    # __init__ is a method to declare varaibles 
        self.name='sandeep'
    def print_name(self):
        global age
        return f'my name is {self.name} my age {age}'
    def print_age(self):
        return self.print_name()

object= MyClass()
print(object.print_age())