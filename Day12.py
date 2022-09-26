print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?")
print("What language are we writing in?")
ans1 = input()
if ans1 == "python" or ans1 == "Python":
  print("Correct")
else:
  print("Nope🙈")
print("Which lesson number is this?")
ans2 = int(input())
if(ans2>12):
  print("We're not quite that far yet")
elif(ans2<12):
  print("We've gone well past that!")
elif(ans2==12):
  print("That's right!")
else:
  print("Try again.")
