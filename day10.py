'''#conditional statement(if condition):
tamil=int(input('tamil mark:'))
#english=int(input('english mark:'))
#maths=int(input('maths mark:'))
#science=int(input('science mark:'))
#social=int(input('social mark:'))
if tamil>=90 and tamil<=100:
  print("grade 0")
elif tamil>=80 and tamil<=89:
  print("grade a")
elif tamil>=70 and tamil<=79:
  print("grade b")
elif tamil>=60 and tamil<=69:
  print("grade c")
elif tamil>=50 and tamil<=59:
  print("grade d")
elif tamil>=1 and tamil<=49:
  print("fail")
else:
  print('enter valid mark')'''

age=19
weight=59
if age>15:
  print('eligible')
  if weight>50:
    print('eligible')
  else:
    print('not eligible')
else:
  print('not eligible')
