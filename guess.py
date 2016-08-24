# Use random for random selecting a number
import random

# Variables
minNumber = 1
maxNumber = 100
magicNumber = random.randint(minNumber, maxNumber)
guesses = 0
found = False

print("Guess the Magic Number!")
print("")

# String formatting as a tuple
message = "The Magic Number is between {0} and {1}"
print(message.format(minNumber, maxNumber))

# Loop forever until correct number is guessed
while not found:
    # while, try, except for valid numbers
    while True:
        try:
            print ("Please guess a number: ")
            number = int(input())
            break
        except ValueError:
            print("Please enter a valid number...")    

    # Keep track of guess attempts
    guesses += 1

    # Number guessed
    if number == magicNumber:
        message = "You guessed the right number in {0} guesses!"
        print(message.format(guesses))
        break;

    # Guess is low
    if number < magicNumber:
        print ("Your guess is low.")

    # Guess is high
    if number > magicNumber:
        print ("Your guess is high.")
