import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print i
chosen_letter = random.choice(word_list)
print(chosen_letter)


# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input( "Enter a value :").lower()
print(guess)


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
for letter in  chosen_letter:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")


