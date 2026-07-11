import random
import math

number = random.randint(1, 100)
print(f"Today's lucky number is: {number}")

print(math.pi)
print(math.sqrt(144))
squared = math.pow(5, 2)
print(squared)

#Game
secret = random.randint(1, 10)
guess = int(input("Guess the number 1 to 10: "))
attempts = 1

while guess != secret:
    if guess > secret:
        guess = int(input("Lower: "))
        attempts += 1
    else:
        guess = int(input("Higher: "))
        attempts += 1

print("Correct!")
print(f"You guessed in {attempts} attempts")