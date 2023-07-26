#print(open('workfile','w'))


with open ('workfile') as f:
    read_data=f.read()
f.read="sample test"

for line in f:
    print(line , end=' ')