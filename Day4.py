print(
    "Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!"
)
print()
Name = input("What is your name? ")
Enemy = input("What is your worst enemy’s name? ")
Superpower = input("What is your superpower? ")
Home = input("Where do you live? ")
Food = input("What is your favorite food? ")
print("Hello", Name, "! Your ability to", Superpower,
      " will make sure you never have to look at", Enemy, "again. Go eat",
      Food, "as you walk down the streets of", Home, "and use", Superpower,
      "for good and not\033[31m evil!")
