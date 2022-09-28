print("Try to guess the missing word!")
counter = 0
while True:
  print("Never going to ____ you up")
  answer = input()
  if answer == "give":
    break
  else:
    counter += 1
    print("Try again!")
print("Correct! Only took you", counter, "times!")
