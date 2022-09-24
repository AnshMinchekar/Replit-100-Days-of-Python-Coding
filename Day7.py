print("Hello there!")
print("Have you read any books by Haruki Murakami?")
Answer = input()
print("................")
if Answer == "Yes":
    print("Which one?")
    book = input()
    if book == "Norwegian Wood":
        print("Really? What was the protagonist's name again? ")
        protagonist = input()
        if protagonist == "Toru":
            print("Oh right!")
        else:
            print("I don't think that was his name!")
    elif book == "South of the border west of the sun":
            print("Oh that was a good read too! Do you remember the name of the female protagonist?")
            protagonist = input()
            if protagonist == "Shimamoto":
              print("Oh right!")
            else:
              print("I don't think that was her name!")
else:
    print("You should! They're great if you like slice of life genre!")
