class Person():
    def __init__(self,name,age,job) -> None:
        self.name=name
        self.age=age
        self.job=job
    def print_name(self):
        print(self.name)


sandeep = Person("sandeep",26,"software")

class Child(Person):
    pass


sandy = Child("sandy",26,"doctor")

sandy.print_name()