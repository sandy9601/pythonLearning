def f(a,L=None):
    if L is None:
        L=[]
    L.append(a)
    return L
# i=5
print(f(1))
# print(f(2))
# i=6
# def fe(arg=i):
#     print(arg)
# fe()
print(f(3))
