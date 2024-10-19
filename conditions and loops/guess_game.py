import random

def play_game():
    print("Guess the number from the range, and if you choose the same number as I do, you win!")
    print("1 = 0-9")
    print("2 = 0-100")
    print("Remember, the higher the range, the higher the reward!")
    
    user_input = int(input("Pick the range (1 for 0-9, 2 for 0-100): "))
    
    if user_input == 1:
        user_guess = int(input("Pick a number from 0-9: "))
        system_number = random.randint(0, 9)  # Generate random number in 0-9
    elif user_input == 2:
        user_guess = int(input("Pick a number from 0-100: "))
        system_number = random.randint(0, 100)  # Generate random number in 0-100
    else:
        print("Invalid input.")
        return  # Exit the function if input is invalid

    # Compare user's guess with the system-generated number
    if user_guess == system_number:
        print(f"Congratulations! You guessed it right. The number was {system_number}.")
    else:
        print(f"Sorry, you lost. The correct number was {system_number}.")

def main():
    ask = int(input("Hey, would you like to play a guessing game? (1 = Yes, 0 = No): "))
    
    if ask == 1:
        while True:
            play_game()
            
            # Ask if they want to play again (just for the guessing part)
            retry = int(input("Do you want to guess again? (1 = Yes, 0 = No): "))
            if retry == 0:
                print("Thank you for playing! Goodbye.")
                break  # Exit the loop if user chooses not to guess again
    else:
        print("Okay, bye!")

# Run the game
main()
