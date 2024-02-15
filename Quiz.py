print("Welcome to my computer quiz!")

playing = input("Do you want to play quiz? ")
if playing != "yes":
    quit()

print("Okay! Let's play :) ")

score=0

answer = input("What does EC2 stands for? ")
if answer.lower() == "elastic cloud compute":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PWD stands for? ")
if answer.lower() == "present working directory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the command for creating new directory? ")
if answer.lower() == "mkdir":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which package manager used in ubuntu? ")
if answer.lower() == "apt":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("Your score is: "+ str(score))