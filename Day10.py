bill = float(input("Total amount on the bill: "))
tip = float(input("Percent of tip: "))
People = int(input("Number of people: "))
tip = bill * (tip / 100)
amount = (bill + tip) / People
print("Amount to be paid by each person: ", amount)
