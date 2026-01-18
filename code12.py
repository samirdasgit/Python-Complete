a=int(input("Please enter 1st no: "))
b=int(input("Please enter 2nd no: "))
c=int(input("Please enter 3rd no: "))
if(a>b & a>c):
  print("Large no is",a)
elif(b>a & b>c):
  print("Large no is",b)
else:
  print("Large no is",c)



a=int(input("Please enter 1st no: "))
b=int(input("Please enter 2nd no: "))
c=int(input("Please enter 3rd no: "))
print(max(a,b,c))