class Parent():
    def print_parent(self):
        print("from parent")

p=Parent()

p.print_parent()


class Child(Parent):
    def print_parent(self):
       print("from child")
c=Child()
c.print_parent()
