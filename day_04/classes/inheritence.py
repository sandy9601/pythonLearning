from dataclasses import dataclass
@dataclass(order=True)
class Person():
    name:str
    age:int
    height:float
    email:str
def print_name(name,age):
    print(name,age)

c= Person("sandeep",27,5.6,"sandy@gamail.com")
@dataclass
class Man(Person):
    pass

d=Man("sana",28,5.8,"example@gmail.com")

print(d.print_name("sana",28))








