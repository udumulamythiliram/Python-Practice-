import random
def main():
    print("Welcome to number guessing game!")
    print("You have 10 attempts to guess the right number")

    level = (input("Enter the level { easy , medium , hard }")).lower()

    match level:
        case "easy":
            max_number = 100
            max_attempts = 10
        case "medium":
            max_number = 500
            max_attempts = 15
        case "hard":
            max_number = 1000
            max_attempts = 20
        case _:
            print("invalid")
            return
    
    wins = 0
    loss = 0
    games_played = 0
    ch = "yes"
    while ch == "yes":

        number = random.randint(1,max_number)
        attempts = 0

        while True:
        
        
            try:
                guess = int(input("Enter your guess:"))
                attempts += 1
                    
                if attempts >= max_attempts:
                    print(f"You lost , the number was {number}")
                    loss += 1
                    games_played += 1
                        
                    break
                print(f"remaining attempts {max_attempts - attempts}")

                if guess < number:
                    print("Too low")
                elif guess > number:
                    print("Too high")
                else:
                    print("correct")
                    wins += 1
                    games_played += 1
                    break
            except ValueError:
                print("Invalid input ")
        ch = input("Play again? (yes/no)").lower()

   
    
    print(f"Games played:{games_played}")
    print(f"Won: {wins}")
    print(f"Lost: {loss}")        


 
        


    
main()
