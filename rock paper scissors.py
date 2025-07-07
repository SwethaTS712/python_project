import random
print("           welcome to Rock Paper Scissors Game         " )

rock=('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''')
paper=('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

''')
scissors=('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
user =int( input("enter your choice 1-rock , 2-paper, 3-scissors ")) 
computer = random.randint(1,3)

if user==1:
    print(rock +"/n your choice/n")
    if computer == 1:
        print(rock +"/ncomputer choice is rock /n game is draw now !!!")
    elif computer == 2:
        print( paper +"/ncomputer choice is paper /n computer won the game !!!")
    else:
          print(scissors +"/ncomputer choice is scissors /n you won the game !!!")
     
elif user == 2:
    print(paper   + "/n your choice/n")

    if computer ==1:
        print(rock +"/ncomputer choice is rock /n you won the game !!!")
    elif computer == 2:
        print( paper +"/ncomputer choice is paper /n game is draw now !!!")
    else:
        print(scissors +"/ncomputer choice is scissors /n computer won the game !!!")

elif user==3:
    print(scissors  + "/n your choice/n")
    if computer == 1:
        print(rock +"/ncomputer choice is rock /n computer  won the game !!!")
    elif computer == 2:
         print( paper +"/ncomputer choice is paper /n you won the game !!!")
    else:
          print(scissors +"/ncomputer choice is scissors /n game is draw now !!!")


else:
    print("invalid choice")
