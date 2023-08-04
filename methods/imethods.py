class Student:
    school = "albanero"
    def __init__(self,m1,m2,m3) -> None:
      self.m1=m1
      self.m2=m2
      self.m3=m3
    
    """ instance method is refered to individual objects"""

    def avg(self):
       return (self.m1+self.m2+self.m3)/3
    @classmethod
    def get_school(cls):
       return cls.school
    @staticmethod   #  @staticmethod is used for generic independent on class and instance
    def print_info():
       print("in this class there are 150 members are there")



s1=Student(30,35,36)
s2=Student(37,40,58)

print(Student.get_school())
print(s1.get_school())

Student.print_info()
s1.print_info()