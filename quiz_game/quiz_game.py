print("Welcome to  my computer quiz !")

playing = input("Do you want to play? ")
score = 0
if playing.lower() == "no":
    quit()
else:
    print("Okay let's play :)")
answer = input("what does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does RAM stands for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does psu stands for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + "questions correct!")
print("You got " + str((score / 4)*100) + "%.")
