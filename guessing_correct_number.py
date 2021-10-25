import random

top = input("Type a number: ")

if top.isdigit():
    top = int(top)

    if top <= 0:
        print('Please type a number larger than 0 for the next time')
        quit()
else:
    print('Please type a number for the next time')
    quit()

random_num = random.randint(0, top)
guesses = 0

while True:
    guesses += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Please type a number for the next time ')
        continue

    if guess == random_num:
        print("You got it!")
        break
    elif guess > random_num:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")