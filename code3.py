def switch_example(value):
  match value:
    case 1:
      return "Option 1 selected"
    case 2:
      return "Option 2 selected"
    case 3:
      return "Option 3 selected"
    case _:
      return "Invalid option"

val1=int(input("Enter value: "))
print(switch_example(val1))