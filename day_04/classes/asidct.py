from dataclasses import dataclass , asdict
@dataclass

class Point:
    x:int
    y:int

@dataclass

class C:
    mylist: list[Point]
p=Point(10,20)

assert asdict(p) == {'x':10,'y':20}

c=C([Point(0,0),Point(10,4)])

assert asdict(c) == {'mylist':[{'x':0,'y':0},{'x':10,'y':4}]}

print(c)