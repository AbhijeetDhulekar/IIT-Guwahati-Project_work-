import random

Player_choice = int(input("Enter your choice here: Type 0 for rock, 1 for paper, and 2 for scissors."))
if Player_choice >= 3 or Player_choice <= 0:
    print("You entered invalid number, try again.")
else:
    computer_choice = random.randint(0,2)
    print("Computer_Chose: ")
    print(computer_choice)
    if computer_choice == Player_choice:
        print("It's a draw.")
    elif computer_choice > Player_choice:
        print("You Lose.")
    elif Player_choice > computer_choice:
        print("You Win.")
    elif computer_choice == 0 and Player_choice == 2:
        print("You Lose.")
    elif Player_choice == 0 and computer_choice == 2:
        print("You Win.")


