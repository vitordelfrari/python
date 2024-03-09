print("Welcome to the Shopping Cart Program!")
print()

cart = []
prices = []
item = ("")
price = ("")

def opitions():
    print("Your option are:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")


while True:
    opitions()
    choice = input("Please enter the number of your action: ")
    if choice == "5": 
        print()
        print("Thank you. Goodbye.")
        print()  
        break
    
    elif choice != "0":
        if choice == "1":
            item = input("What item would you like to add? ")
            cart.append(item)
            while True:
                try:
                    price = float(input(f'What is the price of "{item}"? '))
                    if not 0 <= price <= 99999999999:
                        raise ValueError("You need to type the price of the product: ")
                except ValueError as e:
                    print("You need to type the price of the product: ")
                else:
                    prices.append(price)
                    print(f'"{item}" has been added to the cart')
                    print()
                    break
        
        elif choice == "2":
            print()
            print("The contents of the shopping cart are:")
            for i in range(len(cart)):
                cart_item = cart[i]
                prices_item = prices[i]
                print(f"{i + 1}. {cart_item} - $ {prices_item:.2f}")
            print()
                
        elif choice == "3":
            print()
            remove = int(input("Type the number of the item you want to remove: "))
            remove = int(remove - 1)

            for i in range(len(cart)):
                if remove == i:
                    cart.pop(remove)
                    prices.pop(remove)
                    print("Item removed")
                    print("Your shopping cart now have: ")
                    for i in range(len(cart)):
                        cart_item = cart[i]
                        prices_item = prices[i]
                        print(f"{i + 1}. {cart_item} - $ {prices_item:.2f}")
                    print()
                    break

                else:
                    print()
                    print("This number item is not in your list.")
                    print()

        elif choice == "4":
            print()
            print(f"The total of your cart is: $", format(sum(prices), ",.2f"))
            print()
            
        else:
            print()
            print("Type a valid option")
            print()


