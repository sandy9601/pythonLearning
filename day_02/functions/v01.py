def feb(n):
    "writing a febinoci series"
    a,b = 0,1
    while a < n :
        print(a,end=" ")
        a,b =b,a+b



feb(2000) # if it doesnot return any values it will returns None value 