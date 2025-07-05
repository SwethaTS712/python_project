print ("          welcome to pizzahunt               ")
size = input("what size  pizza do you want s,m or l ?(yes/no)")
pepperoni = input("do you want pepperoni on your pizza (yes/no)")
cheese=input("do you want extra cheese (yes/no)")
amount=0
if size=="s":
    amount+=100
elif size =="m":
    amount+=150
elif size =="l":
    amount+=190
else:
    print("invalid selection")
# pepperoni 
if pepperoni =="yes":
    amount+=50
# cheese
if cheese =="yes":
    amount+=40

print(f"you're pizza cost is {amount}")