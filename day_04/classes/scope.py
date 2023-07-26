def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam="non local spam"
    def do_global():
        global spam
        spam="global spam"
    spam="test spam"
    do_local()
    print("After local assignmen :",spam)
    do_nonlocal()               
    print("After nonlocal assignment : ", spam)
    do_global()
    print("After global assignment:",spam)
#

def name():
    my_name="sandeep"
    print(my_name)

my_name="sandy"
def print_name():
    global my_name
    print(my_name)

print_name()