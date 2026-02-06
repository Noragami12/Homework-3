import random

def play_game():
    print("--- Welcome to Rock, Paper, Scissors! ---")
    
    # Difficulty Selection
    print("\nSelect Difficulty Level:")
    print("1. Normal (Fair game)")
    print("2. Impossible (The computer 'reads your mind')")
    
    mode = input("Enter 1 or 2: ")
    
    options = ["rock", "paper", "scissors"]
    
    # Win conditions: key beats value
    winning_rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    # "Cheating" logic: what the computer picks to beat the player
    counter_moves = {
        "rock": "paper",
        "scissors": "rock",
        "paper": "scissors"
    }

    while True:
        user_choice = input("\nYour move (rock, paper, scissors) or 'quit': ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing! Goodbye.")
            break
            
        if user_choice not in options:
            print("Invalid input. Please try again!")
            continue

        # Computer logic based on mode
        if mode == "1":
            # Normal: purely random choice
            computer_choice = random.choice(options)
        else:
            # Impossible: computer looks at your choice and counters it
            computer_choice = counter_moves[user_choice]

        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif winning_rules[user_choice] == computer_choice:
            print("You win! 🎉")
        else:
            print("You lose. The machine wins! 🤖")

if __name__ == "__main__":
    play_game()