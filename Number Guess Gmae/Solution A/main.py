import random



random_number = random.randint(1, 100)

def validate_input(guess_number):
    if not guess_number.isdigit():
        print('Invalid input. please try again, your guess should be  an integer')
        return False
    guess_number = int(guess_number)
    if guess_number > 100 or guess_number < 1:
        print("Your guess is out of range! please try again, your guess should be between 1 and 100")
        return False
    return True


def main():
    score = 100
    while True:
        guess_number  = input('Please enter a number: ')
        if guess_number == 'q':
            print('Thenks for playing! Googbye.')
            break
        if not validate_input(guess_number):
            continue

        guess_number = int(guess_number)
        if guess_number > 100 or guess_number < 1:
            print("Your entry is out of range. Please enter a number between 1 and 100.")
        if guess_number > random_number:
            print("Too high! Try again")
        elif guess_number < random_number:
            print("too low! Try again")
        else:
            print('congratulations! you win!')
            print(f'Your score is {score}')
            break
        score -= 10
        score = max(score, 0)


if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number I'm thinking of between 1 and 100.") 
    print("You can type 'q' to quit the game at any time.")
    print("Good luck!")
    print("Let's start the game!")
    main()
