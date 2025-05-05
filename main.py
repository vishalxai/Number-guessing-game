#Number Guessing project
def game():
    from art import logo
    print (logo)
    import random
    random_number=random.randint(1,100)
    Easy_level_attempts = 10
    Hard_level_attempts = 5

    print ("welcome to the number Guessing game! ")
    your_choice=input(f"I am thinking of a number between 1 to 100.choose a difficulty .Type 'easy' or 'hard': " )
    if your_choice == "easy":
        attempts = Easy_level_attempts
    elif your_choice == "hard":
        attempts = Hard_level_attempts
    else:
        print("Invalid input ")

    while attempts > 0 :
        guess = int(input("Make a guess :"))
        if guess  == random_number:
            print(f"you got it ! the answer was {random_number}.")
            break
        elif guess > random_number :
            print("The no is too high: ")
        else:
            print ("Too low: ")

        attempts -= 1
        print(f"you have {attempts} attempts remaining .")

        if attempts == 0 :
            print(f"you have run out of guesses.The number was {random_number}.")
#call game
while True:
    game()
    play_again = input ("Do you want to play again ?Type 'y' or 'n' :")
    if play_again.lower() != 'y':
        print("Thanks for playing! Goodbye ")
        break