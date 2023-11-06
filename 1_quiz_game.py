print("Welcome to my computer!")

playing = input("Do you wat to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay Let's play :) ")
score =  0

answer = input("What is CPU stands for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What is GPI stands for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What is RAM stands for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What is PSU stands for? ")
if answer.lower() == "power supply":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    
print("you got" + str(score)+ "question correct!")
print("you got" + str((score / 4) * 100) + " %.")