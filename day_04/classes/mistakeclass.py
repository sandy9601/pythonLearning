class Dog:
    tricks=[]     # this is bad practice for craeting empty class lists  
    def __init__(self,name) -> None:
        self.name=name
    def add_trick(self,trick):
        self.tricks.append(trick)   

dog1=Dog("german")
dog2=Dog("husky") 

dog1.add_trick("playdead")


print(dog2.tricks)