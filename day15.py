#builtin functions
#import builtins
#print(dir(builtins))

#bultins
#(quotient,remainder)
p=divmod(10,5)
print(p)
#absolute value
print(abs(-4))
#boolean value
print(bool(4))
print(bool(-5))
print(bool(0))
#enumerate
a='vasanth'
for i in enumerate(a):
    print(i)
#evaluvate
print(eval('7+6'))
#length
print(len(a))

for i in range (len(a)):
    print(i,a)
#power
print(pow(4,2))
#reversed
for i in reversed (a):
    print(i)
    
#factorial with import math function    
import math
print(math.factorial(5))





