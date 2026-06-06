import random


choices = ["rock", "paper", "scissor"]

won = 0
lost = 0
draw = 0
ch = "yes"
while ch == "yes":
    computer = random.choice(choices)
    my_choice = input("Your Turn:").lower()
    print(f"computer: {computer}")

    if computer == "rock":
        if my_choice == "paper":
            print("You won")
            won += 1
        elif my_choice == "rock":
            print("Draw")
            draw +=1
        else:
            print("You lost")
            lost +=1
    elif computer == "paper":
        if my_choice == "scissor":
            print("You won")
            won +=1
        elif my_choice == "paper":
            print("Draw")
            draw +=1
        else:
            print("You lost")
            lost +=1
    elif computer == "scissor":
        if my_choice == "rock":
            print("You won")
            won +=1
        elif my_choice == "scissor":
            print("Draw")
            draw +=1
        else:
            print("You lost")
            lost +=1

    ch = input("Play agin? (yes/no)")

print(f"Won: {won}")
print(f"Lost:{lost}")
print(f"Draw:{draw}")
        
   

