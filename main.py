
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

    if(computer == -1  and you == 1 ):
        print("You win!")
        
    elif(computer == -1 and you == 0):
        print("You Lose!")

    elif(computer == 1  and you == -1 ):
        
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win!")
        
    elif(computer == 0  and you == -1 ):
        print("You lose!")
    elif(computer ==0 and you ==1):
        print("You win!")

    else:
        print("oops something went wrong")
        
        
#USING LOGIC (COMPUTER - YOU)
if((computer-you) == -1 or (computer - you) == 2):
    print("you lose")
else:
    print("you win")