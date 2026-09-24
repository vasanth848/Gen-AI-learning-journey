#table excercise
for i in range(1,11):
   print("6*",i,"=",i*6)

for i in range(2,11,2):
   print('6*',i,'=',i*6)
    
#TUPLE
l=tuple('vasanth')
print(l)
print(l.count('a'))
print(len(l))
#print(l.pop(l))
#here we change tuple to list for pop method
t=list(l)
print(t)
t.pop()
print(t)
l=tuple(t)
print(l)
#methods of tuple
#there are only two methods available for tuple
print(l.count('v'))
print(l.index('v'))






