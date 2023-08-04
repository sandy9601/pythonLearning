# generators yeild one at a time saves memory effiecint 

# where a list saves memo

def print_fib(n):
    a=b=1
    for i in range(n):
        print(a)
        a,b=b,a+b




def fibno(n):
    a=b=1
    for i in range(n):
        yield a
        a,b=b,a+b
# for x in fibno(100):
#     print(x)

print_fib(100)