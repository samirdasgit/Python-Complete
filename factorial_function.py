n=int(input ("Enter A +ve Number: \n")) 
def fibonacci_func(m):
   if m==1:
     return 0
   elif m==2 or m==3:
     return 1
   else:
    return fibonacci_func(m-1) + fibonacci_func(m-2)
for x in range(1, n+1):
  print(fibonacci_func(x))
