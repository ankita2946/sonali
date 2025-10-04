import random

def play():
    choice = ["rock", "paper", "scissor"]
    user = input("Enter your choice (rock, paper, scissor): ").lower()

    if user not in choice:
        print("Invalid choice")
        return  # exit the function

    computer = random.choice(choice)
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissor") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissor" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

# Run the game
play()
