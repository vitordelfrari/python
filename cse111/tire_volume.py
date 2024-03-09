import math
import datetime

width = int(input("Enter the width of the tire in mm (ex 205): "))
ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * (width ** 2) * ratio * (width * ratio + 2540 * diameter))/10000000000

print(f"The approximate volume is {volume:.2f} liters")

buy_option = input("Would you like to buy tires with this dimensions? (YES/NO): ").upper()

if buy_option == "YES":
    phone = input("Type your phone number: ")
    print("Thank you. We will call you as soon as possible.")

    current_date = datetime.date.today()

    with open("volumes.txt", "a") as file:
        # Append the values to the end of the file
        file.write(f"{current_date}, Width: {width:.2f}, Aspect Ratio: {ratio:.2f}, Diameter: {diameter:.2f}, Volume: {volume:.2f} - Phone: {phone}\n")

else:
    print("Thank you.")
    current_date = datetime.date.today()

    with open("volumes.txt", "a") as file:
        # Append the values to the end of the file
        file.write(f"{current_date}, Width: {width:.2f}, Aspect Ratio: {ratio:.2f}, Diameter: {diameter:.2f}, Volume: {volume:.2f}\n")