print("Hello there!")
print("Welcome to Generation Identifier")
age = int(input("What's your birth year?"))
if age>=1883 and age<=1900:
  print("Lost Generation")
elif age>=1901 and age<=1927:
  print("Greatest Generation")
elif age>=1928 and age<=1945:
  print("Silent Generation")
elif age>=1946 and age<=1964:
  print("Baby Boomers")
elif age>=1965 and age<=1980:
  print("Generation X")
elif age>=1981 and age<=1996:
  print("Millennials")
elif age>=1997 and age<=2012:
  print("Generation Z")
elif age>=2012:
  print("Greatest Generation")
else:
  print("Incorrect Age. Please try again")
