print("Welcome To the G.K challenge")
ask=input("You wanna play the game? ")
if ask.lower()!="yes":
    quit()
print("Okay let's  play the game :) ")

score=0
answer= input("Who is our Prime minister? ")
if answer.lower()== "narendra modi":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer= input("Who is our Home minister? ")
if answer.lower()== "amit shah":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer= input("Who is our External Affairs minister? ")
if answer.lower()== "s jaishankar":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer= input("Who is our Transport minister? ")
if answer.lower()== "nitin gadkari":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer= input("Who is our Defence minister? ")
if answer.lower()== "rajnath singh":
    print("Correct")
    score+=1
else:
    print("Incorrect")

print("Your "+ str(score)+ " Answers are correct!" )