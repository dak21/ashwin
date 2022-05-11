import random

def swg(computer,mine):
    if (computer==mine):
        return None
    if(computer=='s' and mine=='g'):
        return True
    elif(computer=='w' and mine=='s'):
        return True
    elif(computer=='g' and mine=='w'):
        return True
    else:
        return False


choice=('s','w','g')
computer=random.randint(0,2)
computer=choice[computer]
mine=input("choose either s,w,g :")

win=swg(computer,mine)
print(f"you choose  {mine} and computer choose {computer}")

if win is None:
    print("game draw")
    
elif win:
        print("you won")

else:
        print("you loose")