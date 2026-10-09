import random 
choice = [1,2,3,4,5,6]
x= random.choice(choice)
o= random.choice(choice)
while  True:
     z = (input("enter y for play enter n for quit the game "))
     if z=="y": 
        print(f"yor dice numbers are print{x}    {o}")
     elif z=="n":
        print("thanks for playing the game")
     else :
        print("invalid choice ")
        break