import random 
number = random.randint(1, 10)
while True:
    try:
        guess = int(input("Guess the number between 1 and 10 :"))
        if guess < 1 or guess > 10:
            raise ValueError("Guess out of range")
        break
    except ValueError:
        print("Please enter a wild integer between 1 and 10")

if guess == number:
    print("Congratulations! You guessed the number")