def mul(n):
    return lambda x: x*n
mul1=mul(5)
#print(mul1(6))
numbers=[1,2,3,4,5,6,7,8,9,10]
squares = map(lambda x:pow(x,2),numbers)
print(*squares)

# lamda is a anonymos function that returns a function so that we can re use that function mainly it is used in filter and map
