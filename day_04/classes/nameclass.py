class Dog:
    kind='canine'
    def __init__(self,name) -> None:
        self.name=name
german=Dog("german-shepherd")
husk=Dog("husky") 

print({german.name,german.kind})
