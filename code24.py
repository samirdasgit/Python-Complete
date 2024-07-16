sub1=int(input("Enter 1st No:"))
sub2=int(input("Enter 2nd No:"))
resultType=int(input("1 for Sum, 2 for Sub, 3 for Mul & 4 for Div"))
if(resultType==1):
  resultValue=sub1+sub2
  print(resultValue)
elif(resultType==2):
  resultValue=sub1-sub2
  print(resultValue)
elif(resultType==3):
  resultValue=sub1*sub2
  print(resultValue)
else:
  resultValue=sub1/sub2
  print(resultValue)