max_chances = 6
used_chances = 0
secret = "moroni"
underline = "_ "

print(f"Welcome to the word guessing game! \nYou have {max_chances} chances to try to get the word right, good luck! \n")

while max_chances > 0:
    try:
        print(f"You hint is: {guessed}")
    except:
        print(f"You hint is: {underline * len(secret)}")

    guess = input("What is your guess? ")
    max_chances -= 1
    used_chances += 1
    position_letter = -1

    if len(guess) != len(secret):
        print(f"Sorry, the guess must have the same number of letters as the secret word.\nYou have more {max_chances} chances.\n")
        continue
    
    guessed = ""

    for letter in guess:
        position_letter += 1
        if letter == secret[position_letter]:
            guessed += f"{letter.upper()} "
        elif letter in secret:
            guessed += f"{letter.lower()} "
        else:
            guessed += "_ "
    
    if guess.lower() == secret.lower():
        print(f"Congratulations! You guessed it!\nIt took you {used_chances} guesses.\n")
        break
    elif max_chances >= 1:
        print(f"You have more {max_chances} chances.\n")
    elif max_chances == 0:
        print("Your chances are expired, you lost! :(")
