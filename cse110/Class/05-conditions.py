n_1 = int(input('Write a integer number, please: '))
n_2 = int(input('Write another integer number, please: '))

if n_1 > n_2:
    print ('The first number is greater.')
else:
    print ('The first number is not greater.')
if n_1 == n_2:
    print ('The numbers are equal.')
else:
    print ('The numbers are not equal')
if n_1 < n_2:
    print ('The second number is greater.')
else:
    print ('The second number is not greater.')

animal = (input('What is your favorite animal? '))

if animal.lower() == "wolf":
    print ("That's my favorite animal too!")
else:
    print ("That one is not my favorite.")