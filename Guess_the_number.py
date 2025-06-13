import random

print("I am thinking of a number between 1 and a 100. Can you Guess it?")
random_number = random.randint(1, 100)
attempts = 0
while True:
    try:
        Guess = int(input("Can you guess a number: "))
        attempts = attempts + 1
        if attempts < 7:
            if Guess == random_number:
                print("Correct!")
                break
            elif Guess > random_number:
                print("your guess is too high")
            elif Guess < random_number:
                print("your Guess is too low")
        else:
            print("too many attempts,the number was", random_number)
            break
    except ValueError:
        print("This number is not between 1 and a 100")
