import random

def gamewin(comp, you):
    if(comp == you):
        return None
    elif(comp == "Rock"):
        if(you == "s"):
            return False
        elif(you == "p"):
            return True
    elif(comp == "Paper"):
        if(you == "r"):
            return False
        elif(you == "s"):
            return True
    elif(comp == "Scissors"):
        if(you == "p"):
            return False
        elif(you == "r"):
            return True
      
print("Computer's turn: ")
randnum = random.randint(1,3)
if(randnum == 1):
    comp = "Rock"
elif(randnum == 2):
    comp = "Paper"
elif(randnum == 3):
    comp = "Scissors"

you = input("Your turn: Rock(r), Paper(p), Scissors(s)")
a = gamewin(comp, you)

print("Computer chose: "+comp)
print("You chose: "+you)

if a == True:
    print("You Win!")
elif a == False:
    print("You Lose")
else:
    print("It's a Tie") 

