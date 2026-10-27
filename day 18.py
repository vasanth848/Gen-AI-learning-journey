#file handling
f=open('vasanth.txt', 'w+')
cars=('Bmw ','Ferari ','Maserati ','Lamborghini ','Porsche')
f.write(str(cars))
f.close()

def rat(f):
    for i in range(0, 6):
        for j in range(i):
            print('*', end=' ', file=f)
        print(file=f)

f = open('vasanth.txt', 'a+')
rat(f)
f.close()

#here i use with method to aviod close() operation
with open('vasanth.txt') as f:
    print(f.read(5))
    
#we access files from different locations also
#by giving absolute path and relative path
with open(r'C:\Users\acer\Desktop\hello world.py') as l:
   print(l) 
