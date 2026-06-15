number = int(input("Please enter a number: "))
numbers = []
suffix = ["1st", "2nd", "3rd"]

for i in range(number):
    current_count = i + 1  # Offset the 0-index for accurate counting
    
    if current_count <= 3:
        msg = f"Enter {suffix[i]} number: "
    else:
        # Use current_count instead of i
        msg = f"Enter {current_count}th number: " 
        
    num = int(input(msg))
    numbers.append(num)

maxNumber = max(numbers)
numbers.remove(maxNumber)

print(numbers)