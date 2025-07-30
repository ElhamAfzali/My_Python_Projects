import random


class RockPaperScissors():
    def __init__(self, name):
        self.name = name
        self.choices = ['rock','paper', 'scissors']

    def get_computer_choice(self):
        return random.choice(self.choices)


    def get_user_choice(self):
        user_choice = input(f"please enter your choice ({self.choices}): ")
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        print(f"Invalid choice! You must choose fron ({self.choices})")
        return self.get_user_choice()

    def decide_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        win_combinations = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]
        for win_comb in win_combinations:
            if (user_choice == win_comb[0]) & (computer_choice == win_comb[1]):
                return 'Congratulations {self.name}! You won!'
        return "Oh! The computer won!"


    def play(self):
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print(f"user_choice: {user_choice},\ncomputer_choice: {computer_choice}")
        print(self.decide_winner(user_choice, computer_choice))


if __name__ == '__main__':

    game = RockPaperScissors('Elham')
    while True:
        game.play()

        continue_game = input('Do you want to play again? (Enter any key to play again. Enter q/Q to exit!)')
        if continue_game.lower() == 'q':
            break