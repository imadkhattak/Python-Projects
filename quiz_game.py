print("welome to my quiz game")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

print("ok let's play :) ")

score = 0

answer = input("what does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect! The correct answer is 'central processing unit'.")


answer = input("what does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect! The correct answer is 'graphics processing unit'.")


answer = input("what does RAM stand for? ")

if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect! The correct answer is 'random access memory'.")


answer = input("what does SSD stand for? ")

if answer.lower() == "solid state drive":
    print("correct!")
    score += 1
else:
    print("incorrect! The correct answer is 'solid state drive'.")


print("you got " + str(score) + " questions correct!")
print("you got " + str((score / 4) * 100) + "%.")
