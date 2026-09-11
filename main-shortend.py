
import random #IMPORTED MODULE TO GENERATE RANDO VALUE 
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1,0,1])
youstr = input("Enter your choice : ") #FROM 3 ENTER YOUR CHOICE
youDict = {"s" : 1, "w": -1, "g": 0}
reverseDict= {1: "Snake",-1:"Water",0:"Gun"} #(CHOICES) CONVERTED INTO NUMBERS 

you = youDict[youstr]

#BY NOW WE HAVE TWO NUMBERS (VARIABLES),YOU AND COMPUTER
print(f"You chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}")

if(computer == you):    #IF BOTH CHOSE THE SAME THEN IT IS DRAW
        print("Its a Draw")
else:
    if((computer-you) == -1 or (computer - you) == 2):
     print("you lose")
    else:
     print("you win")
