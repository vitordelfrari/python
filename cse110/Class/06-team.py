ride = False

age = int(input("What is the age of the first rider? "))
height = int(input("What is the height of the first rider? "))

if age >= 12 and age < 18:
    golden = input("Does this rider have a golden passport (yes/no)? ")

second_rider = input("Is there a second rider (yes/no)? ")

if second_rider.lower().strip() == "yes":
    age_2 = int(input("What is the age of the second rider? "))
    height_2 = int(input("What is the height of the second rider? "))

    if age_2 >= 12 and age_2 < 18:
        golden_2 = input("Does this rider have a golden passport (yes/no)? ")

    if height < 36 or height_2 < 36:
        ride = False
    
    else:
        if age >= 18 or age_2 >= 18 or golden.lower().strip() == "yes" or golden_2.lower().strip() == "yes":
            ride = True

        else:

            if age >= 12 and age_2 >= 12 and height >= 52 and height_2 >= 52:
                ride = True
            
            elif (age >= 16 and age_2 >= 14) or (age >= 14 and age_2 >= 16):
                ride = True

            else:
                ride = False

else:
    if (age >= 18 or golden == "yes") and height >= 62:
        ride = True

    else:
        ride = False
        
if ride:
    print("Welcome to the ride. Have fun!")
else:
    print("Sorry, you can't ride today.")

# Sample Solution
# """
# File: teach06_sample.py
# Author: Brother Burton

# Purpose: Amusement park ride requirements.
# """
# # Notice the use of a boolean variable, set to False by default
# can_ride = False

# age1 = int(input("What is the age of the first rider? "))
# height1 = int(input("What is the height of the first rider? "))

# if age1 >= 12 and age1 < 18:
#     golden1 = input("Does this rider have a golden passport (yes/no)? ")

# is_second_rider = input("Is there a second rider (yes/no)? ")

# if is_second_rider.lower() == "yes":
#     age2 = int(input("What is the age of the second rider? "))
#     height2 = int(input("What is the height of the second rider? "))

#     if age2 >= 12 and age2 < 18:
#         golden2 = input("Does this rider have a golden passport (yes/no)? ")

#     # Rule 1
#     if height1 < 36 or height2 < 36:
#         can_ride = False
#     else:
#         # Rule 3
#         if age1 >= 18 or age2 >= 18 or golden1.lower() == "yes" or golden2.lower() == "yes":
#             # At least one is an adult
#             can_ride = True
#         else:
#             # Neither is an adult

#             # Rule 4
#             if age1 >= 12 and height1 >= 52 and age2 >= 12 and height2 >= 52:
#                 can_ride = True
#             elif (age1 >= 16 and age2 >= 14) or (age1 >= 14 and age2 >= 16):
#                 # Rule 6
#                 can_ride = True
#             else:
#                 can_ride = False
# else: # There is only one rider
#     # Rule 2
#     if (age1 >= 18 or golden1.lower() == "yes") and height1 >= 62:
#         can_ride = True
#     else:
#         can_ride = False


# if can_ride:
#     print("Welcome to the ride. Please be safe and have fun!")
# else:
#     print("Sorry, you may not ride.")