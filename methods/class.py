class Computer:
    def __init__(self) -> None:
        self.name="dell"
        self.price="50k"
      


    def config(self):
        print("features of computer ",self.name,self.price)
    def update(self):
        self.price="70k"


com1=Computer()
com2=Computer()
com1.update()
print(com1.__dict__)