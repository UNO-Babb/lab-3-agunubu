import random

def main():
    wins = 0
    ties = 0
    losses = 0

    playagain = 'Y'  
    while playagain == 'Y':  # Main game loop
        # Game logic
          computer = random.choice(['R', 'P', 'S'])  # Computer randomly selects
          player = input("Choose your weapon (R, P, S):\n")  # Get player's choice

        # Print the computer's choice
          if computer == 'R':
                print("Computer chose Rock")
          elif computer == 'P':
              print("Computer chose Paper")
          elif computer == 'S':
              print("Computer chose Scissors")

          # Determine the winner
          if player == computer:
              print("It's a tie.")
              ties += 1
          elif player == 'R' and computer == 'S':
              print("You win!")
              wins += 1
          elif player == 'P' and computer == 'R':
              print("You win!")
              wins += 1
          elif player == 'S' and computer == 'P':
              print("You win!")
              wins += 1
          elif player == 'R' and computer == 'P':
              print("You lose.")
              losses += 1
          elif player == 'P' and computer == 'S':
              print("You lose.")
              losses += 1
          elif player == 'S' and computer == 'R':
              print("You lose.")
              losses += 1

          playagain = input("Play again? (Y/N): ").upper() 

    
    print("\nGame over!")
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
    main()