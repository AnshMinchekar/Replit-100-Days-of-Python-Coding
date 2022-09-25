print("Hello there!")
print("What's your name?")
_name = input()
print("Oh! and what're you doing today?")
_work = input()
print("On a scale of 1-10, how happy are you?")
_mood = input()
print("................")
if _mood == "1":
  print("It's going to be alright", _name,"! You have to cheer up after all you have to", _work)
elif _mood == "2":
  print("Ah! No worries! You'll cheer up soon", _name,"! afterall you still have to", _work)
elif _mood == "3":
  print("Nice, looks like you're ready ", _name,"! To handle whatever comes your way today to", _work)
elif _mood == "4":
  print("That's the spirit", _name,"! Let's go and finish up", _work)
elif _mood == "5":
  print("Let's go", _name,"!", _work, "is going to be a piece of cake")
else:
    print("Hm, are you feeling alright?")
