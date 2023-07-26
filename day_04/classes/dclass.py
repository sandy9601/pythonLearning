from dataclasses import dataclass

@dataclass
class Myclass:
    a:int
    b:int=0
    def print_name(self):
        print(self.b)

class MyName:
    def __init__(self,a:int,b:int=0) -> None:
        name="sandeep"
        self.a=a
        self.b=b  
    def print_name(self):
        print(self.b)
test=Myclass(1)

test.print_name()
