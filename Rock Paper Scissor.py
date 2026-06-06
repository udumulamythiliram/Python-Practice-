import random
choices = ["rock", "paper", "scissor"]
print("TIP: You can just enter the first letter if you want ")

difficulty = input("Enter difficulty( FT3 / FT6 / FT10):").lower()


match difficulty:
    case "ft3":
        max_rounds = 5
        rounds_to_win = 3
    case "ft6":
        max_rounds = 10
        rounds_to_win = 6
    case "ft10":
        max_rounds = 19
        rounds_to_win = 10
    case _:
        print("invalid")
        exit()
        




current_streak = 0
best_streak = 0
ch = "yes"
while ch == "yes":
    won = 0
    lost = 0
    draw = 0
    rounds_played = 0

    while rounds_played < max_rounds:
        
        computer = random.choice(choices)
        my_choice = input("Your Turn:").lower()
        print(computer)
        if computer == "rock":

            
            if my_choice == "paper" or my_choice == "p":
                print("You won this round")
                won += 1
                current_streak += 1
                if current_streak > best_streak:
                    best_streak = current_streak

                    
            elif my_choice == "rock" or my_choice == "r":
                print("Draw")
                draw +=1
                current_streak = 0
                
            else:
                print("You lost this round")
                lost +=1
                current_streak = 0


                
        elif computer == "paper":
            if my_choice == "scissor" or my_choice == "s":
                print("You won this round")
                won +=1
                current_streak += 1
                if current_streak > best_streak:
                    best_streak = current_streak

                    
            elif my_choice == "paper" or my_choice == "p":
                print("Draw")
                draw +=1
                current_streak = 0
                
            else:
                print("You lost this round")
                lost +=1
                current_streak = 0
                



                
        elif computer == "scissor":
            if my_choice == "rock" or my_choice == "r":
                print("You won this round")
                won +=1
                current_streak += 1
                if current_streak > best_streak:
                    best_streak = current_streak

                    
            elif my_choice == "scissor" or my_choice == "s":
                print("Draw")
                draw +=1
                current_streak = 0

                
            else:
                print("You lost this round")
                lost +=1
                current_streak =0
                
        rounds_played +=1

        if won == rounds_to_win:
            
            print("YOU WON!!")
            break
        if lost == rounds_to_win:
            print("Computer Won!")
            break

        

        


            
    ch = input("Play agin? (yes/no)")
print(f"YOU: {won}")
print(f"COMPUTER:{lost}")
print(f"Draw:{draw}")
print(f"Your current streak:{current_streak}  Your best streak:{best_streak}")
