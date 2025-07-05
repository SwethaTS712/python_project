print("welcome to tip calculator")
bill = float(input("what was the total bill?"))
tip = int(input("how much tip would you like to give? : 10,12,15"))
persons = int(input("how many people to split the bill?"))
a=(tip/100)*bill + bill
print(f"each person should pay : {round(a/persons,2)}")

