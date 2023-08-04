a=5
b=10

try:
    print(a/b)
    number=int(10)
    print(c)
except ZeroDivisionError as e:
    print("you cannot devide by zero" , e)
except ValueError as b:
    print("invalid inpu ", b)
except Exception as c:
    print("something went wrong" , c)
finally:
    print("from finally ")


# print(dir(Exception))

