score = {"user": 0, "computer": 0}

def main():
    print("Welcome to Rock Paper Scissors!")

    valid_choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in valid_choices:
            print("Invalid choice. Please try again.")
            continue

        import random
        computer_choice = random.choice(valid_choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            score["user"] += 1
        else:
            print("Computer wins!")
            score["computer"] += 1
        play_again = input("Do you want to play again? (Y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            print("Final Score:")
            for key, value in score.items():
                print(f"  {key}: {value}")
            break

if __name__ == "__main__":
    main()