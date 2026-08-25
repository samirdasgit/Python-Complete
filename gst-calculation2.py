productPrice      = int(input("Enter the product price: "))
gstPercentage     = int(input("Enter the GST percentage: "))
storeStateCode    = int(input("Enter the store state code: "))
customerStateCode = int(input("Enter the customer state code: "))
cgstAmount = sgstAmount = igstAmount = 0
if storeStateCode==customerStateCode:
    cgstAmount = sgstAmount = (productPrice * gstPercentage) / 200
    totalPrice = productPrice + cgstAmount + sgstAmount
    print("CGST Amount: ", cgstAmount)
    print("SGST Amount: ", sgstAmount)
    print("Total Price: ", totalPrice)
else:
    igstAmount = (productPrice * gstPercentage) / 100
    totalPrice = productPrice + igstAmount
    print("IGST Amount: ", igstAmount)
    print("Total Price: ", totalPrice)