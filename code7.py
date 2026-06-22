for i in range(10):
  hour=int(input("Enter no. of hours worked: "))
  if(hour>=40):
    otpay = (hour - 40)*120
  else:
    otpay = 0
  print(f"Hours {hour} overtime pay = Rs: {otpay}")