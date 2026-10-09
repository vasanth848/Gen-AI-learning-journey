#lambda functions
#used for small functions with short one line syntax
#but it's not work for big conditions
#its a normal functon
def sq(a,b):
    s= a*b
    return s
print(sq(5,7))

#lambda function
c = [1, 2, 3, 4, 5]
even = lambda a: a % 2 == 0
print(even(4))
print(even(5))

#lambda's buitin functions
#map(used for give condition for every elements in the list)
c=list(map(lambda a: a**2,c))
print(c)

#fiter(return values based on your condition)
c = list(filter(lambda a: a % 2 == 0, c))
print(c)

#sort(arranges elements)
c = [1, 2, 4, 5, 3]
c.sort(key=lambda a: a)
print(c)

