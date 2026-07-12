num = int(input("Enter a number: "))
flag = True
if num > 1:
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      flag = False
      break
  if flag:
    print("Prime Number")
  else:
    print("Not Prime Number")
else:
  print("Not Prime Number")