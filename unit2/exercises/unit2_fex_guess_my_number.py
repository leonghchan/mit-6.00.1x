"""
Create a program that guesses a secret number. 

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer
will guess the user's secret number!
"""

low = 0
high = 100


print("Please think of a number between 0 and 100!")

while True:
    guess = int((high + low) / 2)
    print("Is your secret number " + str(guess) + "?")
    print(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. \
        Enter 'c' to indicate I guessed correctly",
        end=" ",
    )
    user_input = input("")
    if user_input == "h":
        high = guess
    elif user_input == "l":
        low = guess
    elif user_input == "c":
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")
