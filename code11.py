numberExtention=["st","nd","rd","th","th","th","th","th","th"]
arr=[]
for i in range(9):
  a=int(input(f"Enter {i+1}{numberExtention[i]} no : "))
  arr.append(a)
  
arr.append(a)
bigNo=0
for i in arr:
  if(bigNo<i):
    bigNo=i
print(bigNo)