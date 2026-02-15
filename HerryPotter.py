print("the sorting hat".title())
Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0
print("================")
print("Q1) Do you like Dawn or Dusk?\n\t1)Dawn\n\t2)Dusk\n")
answer=int(input("Enter your answer (1-2): "))
if answer==1:
    Gryffindor+=1
    Ravenclaw+=1
if answer==2:
    Hufflepuff+=1
    Slytherin+=1
else:
    print("wrong input")
print("================")
print("Q2) When I’m dead, I want people to remember me as:\n\t1)The Good\n\t2)The Great\n\t3)The Wise\n\t4)The Bold\n")
answer=int(input("Enter your answer (1-4): "))
if answer==1:
    Hufflepuff+=2
elif answer==2:
    Slytherin+=2
elif answer==3:
    Ravenclaw+=2
elif answer==4:
    Gryffindor+=2
else:
    print("Wrong input")
print("================")
print("Q3) Which kind of instrument most pleases your ear?\n\tThe violin\n\t2)The trumpet\n\t3)The piano\n\t4)The drum")
answer=int(input("Enter your answer (1-4): "))
if answer==1:
    Slytherin+=4
elif answer==2:
    Hufflepuff+=4
elif answer==3:
    Ravenclaw+=4
elif answer==4:
    Gryffindor+=4
else:
    print("Wrong input")
print("\n")
print("Slytherins Score is: ",Slytherin)
print("Hufflepuffs Score is: ",Hufflepuff)
print("Gryffindors Score is: ",Gryffindor)
print("Ravenclaws Score is: ",Ravenclaw)

if Gryffindor>=Slytherin and Gryffindor>=Hufflepuff and Gryffindor>=Ravenclaw:
    print("🦁 Gryffindor!")
elif Slytherin>=Hufflepuff and Slytherin>=Ravenclaw:
    print("🐍 Slytherin!")
elif Hufflepuff>=Ravenclaw:
    print("🦡 Hufflepuff!")
else:
    print("🦅 Ravenclaw!")