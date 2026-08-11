mark = int(input("Enter subject mark: "))
if not 0 <= mark <= 100:
  print("Please enter valid mark.")
else:
  grades = ["Fail", "D", "C", "B", "A"]
  print("Grade:", grades[mark // 20])