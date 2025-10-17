import random


def get_user_choice():
    """Get user input and validate it."""
    while True:
        user_input = input("\nEnter Rock, Paper, or Scissors: ").strip().lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("❌ Invalid choice! Please type Rock, Paper, or Scissors.")


def get_computer_choice():
    """Randomly select computer choice."""
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user, computer):
    """Determine the winner of a round."""
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
            (user == "paper" and computer == "rock") or \
            (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"


def play_round():
    """Play a single round of Rock, Paper, Scissors."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\n🧍 You chose: {user_choice.capitalize()}")
    print(f"💻 Computer chose: {computer_choice.capitalize()}")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "tie":
        print("🤝 It's a tie!")
    elif winner == "user":
        print("✅ You win this round!")
    else:
        print("❌ Computer wins this round!")

    return winner


def play_game():
    """Main game loop (best of 3)."""
    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("First to 2 wins (Best of 3) 🏆")

    user_score = 0
    computer_score = 0

    while user_score < 2 and computer_score < 2:
        winner = play_round()

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nCurrent Score: You {user_score} - {computer_score} Computer")
        print("-" * 30)

    # Final results
    if user_score > computer_score:
        print("🎉 You won the game!")
    else:
        print("💻 Computer won the game. Better luck next time!")

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again in ["yes", "y"]:
        play_game()
    else:
        print("👋 Thanks for playing! Goodbye.")


# Run the game
if __name__ == "__main__":
    play_game()
