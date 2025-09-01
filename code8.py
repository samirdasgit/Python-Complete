a=int(input("Enter 1st no: "))
b=int(input("Enter 2nd no: "))
c=int(input("Enter 3rd no: "))
if(a>b):
  if(a>c):
    print(a)
  else:
    print(c)
elif(b>a):
  if(b>c):
    print(b)
  else:
    print(c)
else:
  print(c)