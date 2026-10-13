#quick remainder on loop with pattern program
name='vasanthans'
for i in range(len(name)+1):
    for j in range(i):
        print(name[j], end=' ')
    print()

#code for printing square of list s    
s=[1,2,3,4,5]
b=[]
for i in s:
    b.append(i**2)

print(b)

#iter builtin function
for i in name:
    print(i)

d=iter(name)

print(d.__next__())
print(d.__next__())
print(d.__next__())
print(d.__next__())


