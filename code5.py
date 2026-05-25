numbers = []
suffix = ["1st", "2nd", "3rd"]
for i in range(1,11):
  if i <= 3:
    msg = f"Enter {suffix[i-1]} number: "
  else:
    msg = f"Enter {i}th number: "
    
  num = int(input(msg))
  numbers.append(num)

numbers.sort()

print("Sorted Numbers:", numbers)