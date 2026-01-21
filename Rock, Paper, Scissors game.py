import random
list = ["rock", "paper", "scissor"]

user = input("Choose your choice : ")
computer = random.choice(list)

print("User's choice : ", user)
print("Computer's choice : ", computer)

if user=="rock" and computer=="scissor":
    print("You are the winner")
elif user=="scissor" and computer=="paper":
    print("You are the winner")
elif user=="paper" and computer=="rock":
    print("You are winner")
elif user=="rock" and computer=="rock":
    print("It's tie")
elif user=="paper" and computer=="paper":
    print("It's tie")
elif user=="scissor" and computer=="scissor":
    print("It's tie")
else:
    print("You has lost the game.")