print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
tip = input("What percentage tip would  you like to give? 10, 12 or 15 ")
people = input("How many people to split the bill? ")

before_tip = float(bill) / int(people)
after_tip = before_tip + before_tip * int(tip)

print(f"Each person  should pay ${after_tip}")