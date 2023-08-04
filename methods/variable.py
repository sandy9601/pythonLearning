#   instant variable and class varible
class Car:
    wheels=4   # class varibales and static varibales

    def __init__(self) -> None:
        self.mil=10
        self.model="BMW"

car1= Car()

#print(Car.mil)

print(Car.wheels)