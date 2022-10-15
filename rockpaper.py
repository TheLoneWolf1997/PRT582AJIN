import random


def start_Game():
    computer_point = 0
    player_point = 0
    while True:
        user_action = input("Enter a choice (rock, paper, scissors): ")
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "rock":
            if computer_action == "scissors":
                player_point += 1
                print("Rock smashes scissors! You win!")
            else:
                computer_point += 1
                print("Paper covers rock! You lose.")
        elif user_action == "paper":
            if computer_action == "rock":

                player_point += 1
                print("Paper covers rock! You win!")
            else:
                computer_point += 1
                print("Scissors cuts paper! You lose.")
        elif user_action == "scissors":
            if computer_action == "paper":
                player_point += 1
                print("Scissors cuts paper! You win!")

            else:
                computer_point += 1
                print("Rock smashes scissors! You lose.")


        if (computer_point >= 5) or (player_point >= 5):
            if computer_point > player_point:
                print("computer wins!")
            else:
                print("User wins!")

            print("The players point is:", player_point)
            print("The computers point is", computer_point)
            break
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            print("The players point is:", player_point)
            print("The computers point is", computer_point)


            return (user_action)

if __name__ == '__main__':
    start_Game()
