child_price = float(input("What is the price of a childs meal? "))
adult_price = float(input("What is the price of an adults meal? "))
drink_price = float(input("What is the price of drinks? "))
child = float(input("How many children are there? "))
adult = float(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

child_total = child_price * child
adult_total = adult_price * adult
child_drink = child * drink_price
adult_drink = adult * drink_price
drink_total = child_drink + adult_drink
subtotal = child_total + adult_total + drink_total
sale_tax = (tax_rate / 100) * subtotal
Total = subtotal + sale_tax
print("                                    ")
print("Childs total: $", format(child_total, ",.2f"))
print("Adults total: $", format(adult_total, ",.2f"))
print("Subtotal: $", format(subtotal, ",.2f"))
print("Sales Tax: $", format(sale_tax, ",.2f"))
print("Total: $", format(Total, ",.2f"))
print("                                    ")

paying_amount = float(input("What is the paying amount? "))
change = paying_amount - Total

print("Change: $", format(change, ",.2f"))