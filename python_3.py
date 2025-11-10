printed_price = int(input("Enter Printed Price: "))
discount_percentage = int(input("Enter Discount Percentage(%): "))
Tax_percentage = int(input("Enter Sales Tax(%): "))

Discounted_Price = printed_price - ((printed_price * discount_percentage)/100)
print("Discounted Price: ", Discounted_Price)

After_Tax = Discounted_Price + ((Discounted_Price*Tax_percentage)/100)
print("Final Price: ", After_Tax)


