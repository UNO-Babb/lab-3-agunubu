import random

def main():
    wins = 0
    ties = 0
    losses = 0

    playAgain = 'Y'  
    while playAgain == 'Y':  
        # Game logic
          computer = random.choice(['R', 'P', 'S'])  
          player = input("Choose your weapon (R, P, S):\n")  

        
            if computer == 'R':
                print("Computer chose Rock")
          elif computer == 'P':
              print("Computer chose Paper")
          else computer == 'S':
              print("Computer chose Scissors")

          
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
            playAgain = input("Play again? (Y/N): ")
     

    
    print("\nGame over!")
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
    main()