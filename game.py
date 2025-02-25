import random

def guess_the_number(n):

    while True:
        random_guess = random.randint(1, n)
        guess = 0

        while not guess == random_guess:
            guess = int(input(f"Guess a number between 1 and {n}: "))
            if guess < random_guess:
                print("Your guess is too low!")
            elif guess > random_guess:
                print("Your guess is too high!")

        print("Congrats, you've guessed the number right!")
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        
        if play_again == 'y':
            print("Let's play again!")
              
        elif play_again == 'n':
            print("Goodbye!")
            break
        else:
            print(input("Please enter a valid answer: "))
            

guess_the_number(10)