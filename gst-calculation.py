sellingPrice=int(input("Enter the selling price: "))
gstRate=int(input("Enter the GST rate: "))
gstAmount=round((sellingPrice*gstRate)/100)
print("The amount is:",sellingPrice+gstAmount)