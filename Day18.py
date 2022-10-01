print("Welcome to Guess the number.")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you're too high, too low or get it corrct.")
print()
print("Let's play!")
number = 2500
attempt = 1
while True:
  guess = int(input("Pick a number between 1 and 1,000,000: "))
  if guess < number:
    print("Too low! why not try again?")
    attempt = attempt + 1
  elif guess > number:
    print("Too high! why not try again?")
    attempt = attempt + 1
    continue
  elif guess == number:
    print("That's right!")
    break
  elif guess < 0:
    print("Don't think that's where you wanna go bud.")
    exit()
  else:
    print("Not sure if I know that")
print("You took a total of", attempt,"tries!")
  
