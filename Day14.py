from getpass import getpass as input
print("Welcome to the ultimate 🪨, 📃 & ✂️ Game")
print("..........................................")
print("""
RULES
................
1. Type R for Rock, P for Paper & S for Scissors.
2. Each player only gets one turn.
""")
print("Your move Player 1:")
p1 = input()
print("Your turn Player 2:")
p2 = input()
if p1 == "R" and p2 == "P":
    print("Player 1's 🪨 has been covered up Player 2's 📃 entirely!.")
elif p1 == "P" and p2 == "R":
    print("Player 1's 📃 has covered up Player 2's 🪨 entirely.")
elif p1 == "R" and p2 == "S":
    print("Player 1's 🪨 has crushed Player 2's ✂️ entirely.")
elif p1 == "S" and p2 == "R":
    print("Player 1's ✂️ has been crushed up Player 2's 🪨 entirely.")
elif p1 == "P" and p2 == "S":
    print("Player 1's 📃 has been cut into pieces by Player 2's ✂️ entirely.")
elif p1 == "S" and p2 == "P":
    print("Player 1's ✂️ has cut Player 2's 📃 into pieces.")
elif p1 == "R" and p2 == "R":
    print("Both picked 🪨, it's a draw ")
elif p1 == "S" and p2 == "S":
    print("Both picked ✂️, it's a draw.")
elif p1 == "P" and p2 == "P":
    print("Both picked 📃, it's a draw.")
else:
    print("Try again")
