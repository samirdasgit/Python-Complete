num=int(input("Enter a number: "))
sum = 0
for i in range(1,num+1,2):
  sum+=i
print("Total of Odd: ",sum)

sum = 0
for i in range(2,num+1,2):
  sum+=i
print("Total of Even: ",sum)