exit = "no"
while exit == "no":
  animal_sound = input("What animal sound do you want to hear?")
  
  if animal_sound == "cow" or animal_sound == "Cow":
    print("🐮 Moo")
  elif animal_sound == "dog" or animal_sound == "Dog":
    print("🐶 Woof")
  elif animal_sound == "cat" or animal_sound == "Cat":
    print("🐱 Meow")
  elif animal_sound == "sheep" or animal_sound == "Sheep":
    print ("🐑 Baaa")
  else: 
    print("I don't know that animal sound. Try again.")
  exit = input("Do you want to exit?: ")
