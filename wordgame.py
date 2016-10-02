import random

# Return a random word from a list of words.
def get_random_word():
    words = ["pizza", "apples", "cheese"]
    word = words[random.randint(0, len(words) - 1)]
    return word

# Display a given word on a single line, with spaces
def show_word(word):
    for character in word:
        print(character, " ", end="")
    print("")

# Prompt the player for a letter
def get_guess():
    print("Enter a letter: ")

    # need to add error checking logic here
    return input()

# Take the given letter and see if it exists in the word
# Update the blanked version of the word if it exists
def process_letter(letter, secret_word, blanked_word):
    result = False

    for i in range(0, len(secret_word)):
        if secret_word[i] == letter:
            result = True
            blanked_word[i] = letter

    return result

# Print the number of strikes the player has
def print_strikes(number_of_strikes):
    for i in range(0, number_of_strikes):
        print("X ", end="")
    print("")

# Main game loop
def play_word_game():
    strikes = 0
    max_strikes = 3
    playing = True

    word = get_random_word()
    blanked_word = list("_" * len(word))

    while playing:
        show_word(blanked_word)
        letter = get_guess()
        found = process_letter(letter, word, blanked_word)

        if not found:
            strikes += 1
            print_strikes(strikes)

        if strikes >= max_strikes:
            playing = False

        if not "_" in blanked_word:
            playing = False
            

    if strikes >= max_strikes:
        print("You lose!")        
    else:
        print("You win!")

    print("The word was: " + word)

print("Guess the Word!")
play_word_game()

