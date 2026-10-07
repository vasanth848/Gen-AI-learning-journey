#recursive functions
#fuctions calls inside itself until condition statisfy
def numbers(n):
    if n==0:
        return
    print(n)
    numbers(n-1)

numbers(6)

#(** Keyword args accept mutiple arguments for one paramater with (**)
def student(**details):
    print(details)

student(name="Vasanthan", age=21, course="GenAI")

#(positional arguments)*args uses tuple to store values
#(key word arguments)**Kwargs uses dictionary to store values
def student(name, age=21, *skills, **details):
    print("Name:", name)
    print("Age:", age)
    print("Skills:", skills)
    print("Other details:", details)

student(
    "Vasanthan",
    22,
    "Python",
    "GenAI",
    city="Chennai",
    degree="B.Tech"
)
