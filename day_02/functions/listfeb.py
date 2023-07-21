def feb(n):
    "writing a function to return a feb series in a lists"
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


feb2 = feb(10) # assigning to a variable
print(feb2)
