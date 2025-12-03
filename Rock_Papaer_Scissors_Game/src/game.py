import random


class RockPaperScissors():
    """
    A class for the rock, paper, scissors.

    """

    def __init__(self):
        self.choice = ['rock', 'paper', 'scissors']


    def get_user_choice(self):
        """
        Method to get the user's choice.

        :return: User's choice as a string
        """
        user_choice: str = input(f'Please enter your choice from this list {self.choice}')
        if user_choice.lower() in self.choice:
            return user_choice.lower()
        else:
            print("Invalid choice. Please make sure your choice is in 'rock', 'paper' or 'scissors'.")
        return self.get_user_choice()

    def get_computer_choice(self):
        """Method toget the computer's choice.

        :return: computer's choice as a string
        """
        return random.choice(self.choice)

    def decide_winner(self, user_choice, computer_choice):
        """Method to decide game winner based on the rules.

        :param user_choice: The user's choice
        :param computer_choice: The computer's choice
        :return: Game outcome as a string
        """
        if user_choice == computer_choice:
            return f"It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or\
            (user_choice == 'paper' and computer_choice == 'rock') or\
            (user_choice == 'scissors' and computer_choice == 'paper'):
            return f"Congratulations, you won!"
        else:
            return f"Oh! The computer won!"
    def play(self):
        """Main method to play Rock, Paper, Scissors"""

        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print('Computer chose: ', computer_choice)
        print(self.decide_winner(user_choice, computer_choice))


if __name__ == '__main__':

    game = RockPaperScissors()
    
    while True:
        game.play()
        continue_game = input("Do you want to play again? (Enter any key to continue or 'q' to quit): ")
        if continue_game.lower() == 'q':
            break