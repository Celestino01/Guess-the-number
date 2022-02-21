import random

randomNumberList = []

def numberGenerator():
  for num in range(1, 101):
    randomNumberList.append(num)
  randomNumber = random.choice(randomNumberList)
  return randomNumber

guessingNumber = numberGenerator()

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
levelOfDifficulty = input("Choose a difficulty level. Type 'easy' or 'hard' ")
attempts = 0

if levelOfDifficulty == "easy":
  attempts = 10
  keepGuessing = True
  while attempts > 0 and keepGuessing:
    print(f"You have {attempts} remaining to guess the number ")
    guess = int(input("Make a guess: "))
    if guess == guessingNumber:
      print("Correct! you win!")
      keepGuessing = False
    elif guess > guessingNumber:
      print("Too high")
      attempts -= 1
    else:
      print("Too low")
      attempts -= 1
else:
  attempts = 6
  keepGuessing = True
  while attempts > 0 or keepGuessing:
    print(f"You have {attempts} remaining to guess the number ")
    guess = int(input("Make a guess: "))
    if guess == guessingNumber:
      print("Correct! you win!")
      keepGuessing = False
    elif guess > guessingNumber:
      print("Too high")
      attempts -= 1
    else:
      print("Too low")
      attempts -= 1
  
