print("Welcome to grade calculator")
print("Enter the subject name:")
subject = input()
print("Enter max. number of marks obtainable:")
max = int(input())
print("Enter marks received:")
marks = int(input())
print(".......")
total = float((marks / max) * 100)
percentage = round(total, 2)
if percentage < 60:
    print("Your Percentage in", subject, "=", percentage, "& Your grade: F")
elif percentage >= 60 and percentage <= 69:
    print("Your Percentage in", subject, "=", percentage, "& Your grade: D")
elif percentage >= 70 and percentage <= 79:
    print("Your Percentage in", subject, "=", percentage, "& Your grade: C")
elif percentage >= 80 and percentage < 89:
    print("Your Percentage in", subject, "=", percentage, "& Your grade: B")
elif percentage >= 90 and percentage <= 100:
    print("Your Percentage in", subject, "=", percentage, "& Your grade: A")
else:
    print("Please try again")
