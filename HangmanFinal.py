import random

words = ("apple", "banana", "kumquat", "peach", "pear", "orange")
RemainingGuesses = 6
Answer = random.choice(words)
Hint = ["_"] * len(Answer)
Guessed_letters = set()

print("Welcome to Hangman! Guess the word one letter at a time!")
is_running = True
while is_running:
    print (str(RemainingGuesses) + " guesses remain.")
    print(" ".join(Hint))
    Guess = input("Enter a letter: ").lower()
    if len(Guess) != 1 or not Guess.isalpha():
            print("Invalid input!")
            continue

    if Guess in Guessed_letters:
            print(f"{Guess} was already guessed!")
            continue

    Guessed_letters.add(Guess)

    if Guess in Answer:
        for i in range(len(Answer)):
            if Answer[i] == Guess:
                Hint[i] = Guess
    else:
        RemainingGuesses -= 1

    if "_" not in Hint:
        print("The answer was: "+ str(Answer))
        print("YOU WIN!")
        is_running = False
    elif RemainingGuesses == 0:
        print("The answer was: "+ str(Answer))
        print("YOU LOSE!")
        is_running = False
