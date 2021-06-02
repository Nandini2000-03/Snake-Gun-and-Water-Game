from math import trunc
import random


def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True


    pass

print("Comp Turn : Snake(s),Water(w), and Gun(g)?") 
ranno=random.randint(1,3)
if ranno==1:
    comp='s'
elif ranno==2:
    comp='w'
elif ranno==3:
    comp='g'

you =input("your turn: Snake(s),Water(w), and Gun(g) ? ")
a=gamewin(comp,you)

print(f"Computer chose : {comp}")
print(f"you chose : {you}")

if a==None:
    print("the game is a tie")
elif a:
    print("You Win")
else :
    print("you lose")