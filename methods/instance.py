class Instant():
    class_variable=10
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    
    def print_instance(self):
        print(self.b)
    @classmethod
    def print_class(cls):
        print(cls.class_variable)
# i1=Instant(42,43)

Instant.print_class()