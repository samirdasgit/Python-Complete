buyPrice  = int(input("Enter purchase price: "))
sellPrice = int(input("Enter selling price: "))
if buyPrice>sellPrice:
  print(f"Lose price is {buyPrice-sellPrice}")
else:
  print(f"Profit price is {sellPrice-buyPrice}")