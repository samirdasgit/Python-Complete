subjectMark=int(input("Please enter subject mark: "))
if(subjectMark>100 or subjectMark<0):
  print("Please enter valid mark.")
elif(subjectMark>79):
  print("Grade: A")
elif(subjectMark>59):
  print("Grade: B")
elif(subjectMark>39):
  print("Grade: C")
elif(subjectMark>19):
  print("Grade: D")
else:
  print("Fail")