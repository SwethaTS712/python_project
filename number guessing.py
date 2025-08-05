from random import randint
def simple(num):
    attempts=10
    print(f"you have {attempts} attempts remaining to guess a number")
    while(attempts>0):
        guess=int(input("guess the number: "))
        if guess<num:
            print("to low\n guess again")
             
        elif guess>num:
            print("to high\n guess again")
             
        else:
            print("you got it !!")
            return
        attempts-=1
    print(f"you lost !!!\nthe number is{num} ")

def hard(num):
    attempts=5
    print(f"you have {attempts} attempts remaining to guess a number")
    while(attempts>0):
        guess=int(input("guess the number: "))
        if guess<num:
            print("to low\n guess again")
            
        elif guess>num:
            print("to high\n guess again")
             
        else:
            print("you got it !!")
            return
        attempts-=1
    print(f"you lost !!!\nthe number is{num} ")
         

print("welcome to number guessing game !!!\n i'm guess the number between 1 and 100")
num= randint(1,100)
level=input("choosea difficulty level type easy or difficult: ")
if level == "easy":
    simple(num)
else:
    hard(num)
        



