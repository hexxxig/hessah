import random
print("=============================")
print("Rock Paper Scissors")
print("=============================\n")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
plyer=int(input("Pick a number: "))
if plyer==1:
    print("You chose: ✊")
elif plyer==2:
    print("You chose: ✋")
else:
    print("You chose: ✌️")
computer=random.randint(1,3)
if computer==1:
    print("CPU chose: ✊")
elif computer==2:
    print("CPU chose: ✋")
else:
    print("CPU chose: ✌️")
if plyer==computer:
    print("Its a tie!")
elif plyer==1 and computer==2:
    print("The computer won!")
elif plyer==1 and computer==3:
    print("The plyer won!")    
elif plyer==2 and computer==1:
    print("The plyer won!")
elif plyer==2 and computer==3:
    print("The computer won!")
elif plyer==3 and computer==1:
    print("The computer won!")
else:
    print("The plyer won!")
    
    
    
