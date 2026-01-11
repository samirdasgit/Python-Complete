a=int(input("Enter 1st no: "))
b=int(input("Enter 2nd no: "))
c=int(input("Enter 3rd no: "))
d=int(input("Enter 4th no: "))
e=int(input("Enter 5th no: "))
if(a>b & a>c & a>d & a>e):
  print(a)
elif(b>a & b>c & b>d & b>e):
  print(b)
elif(c>a & c>b & c>d & c>e):
  print(c)
elif(d>a & d>b & d>c & d>e):
  print(d)
else:
  print(e)