from dataclasses import dataclass, field
# dataclasses.field(*, default, default_factory, repr, hash, init, compare, metadata)
@dataclass
class data_class:
    value : int
    title: str = field(default = 'Python3')

class_instance_1 = data_class("10")
print(class_instance_1.title)