#patten program
#square
for i in range(4):
    for j in range(4):
        print('*',end=' ')
    print()
#RAT
for i in range(0,6):
    for j in range(i):
        print("*",end= " ")
    print()
#LAT
for i in range(0,6):
    for j in range (5-i):
        print(" ",end= " ")
    for k in range (i):
        print("*",end= " ")
    print()
#pryamid
for i in range(0,6):
    for j in range (5-i):
        print(" ",end= "")
    for k in range (i):
        print("*",end= " ")
    print()   
 
