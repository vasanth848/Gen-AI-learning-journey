#functions
def functions():
  print('this is function')
functions()

#functions with parameter and arguments 
def my_function(fname):
  print(fname + 'son')
my_function("a")
my_function("b")
my_function("c")

#fuctions with difference between print  and return
#print(simply prints what's inside that)
def add(a, b):
    print(a+b)
x =add(10, 20)
print(x)

#return (return value to function mean to 'parameter' and
#value come when function called)
def add(a, b):
    return(a+b)

x = add(10, 20)
print(x)

def check_number(n):
    if n > 0:
        return("Positive")
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(10))
print(check_number(-5))
print(check_number(0))
