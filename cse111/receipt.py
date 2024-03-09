from datetime import datetime, timedelta
import csv

def main():
    try:
        products_dict = read_dictionary("products.csv", 0)
        print("Vitor's Emporium")
        print()

        total_quantity = 0
        subtotal = 0
        tax = 0
        total = 0

        with open("request.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the first line (column headings)

            for row in reader:
                product_number = row[0]
                product = products_dict.get(product_number)
                if product is not None:
                    product_name = product[1]
                    requested_quantity = int(row[1])
                    product_price = float(product[2])

                    print(product_name, ":", requested_quantity, "@", product_price)
                    total_quantity += requested_quantity  # add the requested quantity to the total
                    subtotal += product_price * requested_quantity
                    tax = subtotal * (6/100)
                    total = subtotal + tax
                else:
                    print("No product found for number:", product_number)

        print()
        print("Number of Items:", total_quantity)

        # Discount on Tuesday or Wednesday
        current_date = datetime.now()
        if current_date.strftime("%A") in ["Tuesday", "Wednesday"]:
            subtotal *= 0.9

        # Discount before 11:00 a.m.
        if current_date.time() < datetime.strptime("11:00 AM", "%I:%M %p").time():
            subtotal *= 0.9

        print("Subtotal: $", format(round(subtotal, 2), ".2f"))
        print("Sales Tax: $", format(round(tax, 2), ".2f"))
        print("Total: $", format(round(total, 2), ".2f"))
        print()

        # Invitation to complete an online survey
        print("Thank you for shopping at the Vitor's Emporium. Please take a moment to complete our online survey.")

    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.")

    except (KeyError) as error: 
        print("Error: The request file is formatted incorrectly.")

def read_dictionary(filename, key_column_index):
    dictionary = {}

    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the first line (column headings)

        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row

    return dictionary


if __name__ == "__main__":
    main()

current_date_and_time = datetime.now()
print(current_date_and_time.strftime("%a %b %d %H:%M:%S %Y"))
