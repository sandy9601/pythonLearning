from dataclasses import  dataclass

class Person:
    def __init__(self,name,age,job) -> None:
        self.name=name
        self.age=age
        self.job=job


@dataclass
class Human:
    name:str
    age:int
    job:str

sandy=Human("sandy",27,"driver")

sandeep=Person("sandeep",26,"software")

print(sandeep)
print(sandy)
