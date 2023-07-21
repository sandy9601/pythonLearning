#range(0,10,3) ==> , 0 to start and till 10 increment 3 
#range(0,10)  ==>  0 to start and till 10 increment by defualt 1
#range(10) == > 0,1,2,3,4,5,6,7,8,9 ==> increment by defualt increment 1 

a=["mary","had","a","little","lamb"]

for i in range(len(a)) : 
    print(i,a[i])