import random
def main():
    balance = int(input("Enter the amount you want to add : "))
    print(f"Your balance is : ${balance} ")
    play = True
    while play:
        action = int(input("1 -> Play\n2 -> CHECK BALANCE\n3 -> ADD MONEY\n4 -> Exit\nEnter your choice : "))
        if action == 1:
            if balance == 0:
                print("You don't have money balance to play..!!")
                break

            bet = int(input("Enter the amount you want to bet : "))
            if bet > balance:
                print("Insufficient balance..!!")
            else:
                balance -= bet
                print(f"Balance : ${balance}")
                number = random.randint(1,6)
                guess = int(input("Enter your guess : "))
                if guess == number:
                    balance += bet * 2
                    print(f"Congratulations..!! You won ${bet * 2}")
                    print(f"Number was : {number}")
                    print(f"Balance : ${balance}")
                else:
                    print(f"You lost number was : {number}")
                    print(f"Balance : ${balance}")
        elif action == 2:
            print(f"Balance : ${balance}")
        elif action == 3:
            add = int(input("Enter the amount you want to add : "))
            balance += add
            print(f"Balance : ${balance}")
        elif action == 4:
            play = False
            break
        else:
            print("Invalid choice..!!")
            continue



if __name__ == '__main__':
    main()  # Call the main function
