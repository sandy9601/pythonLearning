from dataclasses import dataclass, field

@dataclass
class data_class:
    title: str = field(compare = False)
    name: str = field(repr = False)
    language : str = field(default = 'Python3')
    value : int = field(init = False, default = '12')   

class_instance_1 = data_class('Dataclass', 'Studytonight')
class_instance_2 = data_class("Dataclass", "Studytonight")

print(class_instance_1) 
print(class_instance_2) 

print(class_instance_1.value)
print(class_instance_2.language)
print(class_instance_1 == class_instance_2)