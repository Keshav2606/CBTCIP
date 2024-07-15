import random
import time
import os


def load_template():
    print(''' ____            _      ____                       
|  _ \ ___   ___| | __ |  _ \ __ _ _ __   ___ _ __ 
| |_) / _ \ / __| |/ / | |_) / _` | '_ \ / _ \ '__|
|  _ < (_) | (__|   <  |  __/ (_| | |_) |  __/ |   
|_|_\_\___/ \___|_|\_\ |_|   \__,_| .__/ \___|_|   
/ ___|  ___(_)___ ___  ___  _ __  |_|              
\___ \ / __| / __/ __|/ _ \| '__|                  
 ___) | (__| \__ \__ \ (_) | |                     
|____/ \___|_|___/___/\___/|_|          ''')
    
    print("Select:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    print("4. Exit.")

def validate(player, computer):
    global score
    if player == computer:
        print("Its a tie.")
        print(f"Computer chose: {computer}, You chose: {player}")
    elif player == "Rock" and computer == "Paper":
        print("Oops! You Losed.")
        print(f"Computer chose: {computer}, You chose: {player}")
    elif player == "Rock" and computer == "Scissor":
        score += 1
        print("Hurray! You Won.")
        print(f"Computer chose: {computer}, You chose: {player}")
    elif player == "Paper" and computer == "Rock":
        score += 1
        print("Hurray! You Won.")
        print(f"Computer chose: {computer}, You chose: {player}")
    elif player == "Paper" and computer == "Scissor":
        print("Oops! You Losed.")
        print(f"Computer chose: {computer}, You chose: {player}")
    elif player == "Scissor" and computer == "Rock":
        print("Oops! You Losed.")
        print(f"Computer chose: {computer}, You chose: {player}")
    elif player == "Scissor" and computer == "Paper":
        score += 1
        print("Hurray! You Won.")
        print(f"Computer chose: {computer}, You chose: {player}")

    return score


options = ["Rock", "Paper", "Scissor"]
score = 0

while True:
    time.sleep(2)
    os.system('cls')

    load_template()

    computer = random.choice(options)
    print(f"Your Score: {score}")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        player = "Rock"
    elif choice == 2:
        player = "Paper"
    elif choice == 3:
        player = "Scissor"
    elif choice == 4:
        break
    else:
        print("Invalid Input.")

    score = validate(player, computer)
