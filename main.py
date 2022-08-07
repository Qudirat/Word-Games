import random

word_list = ["monkey", "lima", "gorilla", "bunkmate", "glory", "freak", "hippopotamus"]
random_word = random.choice(word_list)
i = len(random_word)
blanks = []
while i > 0:
    blanks.append("_")
    i = i - 1
print(blanks)
print(f"Welcome to the word guess game. The word to guess has {len(blanks)} letters.")
guesses_left = len(blanks) + 2
print(f"You have {guesses_left} guesses.")
while guesses_left > 0:
    user_guess = input("Guess a letter: ").lower()
    if user_guess in random_word and len(user_guess) != 0:
        guess_index = [
            i for i in range(len(random_word)) if random_word[i] == user_guess
        ]
        for index in guess_index:
            blanks[index] = user_guess
        print(blanks)
        if "_" not in blanks:
            print("Congratulations. You guessed the right word.")
            break
    else:
        print(blanks)
        guesses_left -= 1
        print("Letter not in word, try again.")
        print(f"You have {guesses_left} guesses left.")
        if guesses_left == 0:
            print("You have run out of guesses. Try again.")
            break
print("Play another game")

