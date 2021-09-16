import random
def gamewin(comp,you):
     if comp==you:
            return None
     elif comp=='rock' and  you=='paper':
       return True
     elif you== 'sissors':
            return False
     elif comp=='paper' and  you=='rock':
       
            return False
     elif you== 'sissors':
            return True
     elif comp=='sissors' and you=='paper' :
        
            return False
     elif you== 'rock':
            return True

        
randomno= random.randint(1,3)
print(randomno)
if randomno==1:
    comp="Rock"
elif randomno==2:
    comp="Paper"
elif randomno==3:
    comp="Scissors"
you=input("Your Turn: Rock(1) Paper(2) or Scissors(3)?\n\t")



a=gamewin(comp,you)
if you==1:
    print("you chose \nRock")
elif you==2:
    print("you chose \n Paper")
elif you==3:
    print("you chose \n Sissor")


print(f"computer chose:\n{comp}")



if a==None:
    print("game is a tie!")
elif a:
    print("You win!")
else:
    print("You lose!")
