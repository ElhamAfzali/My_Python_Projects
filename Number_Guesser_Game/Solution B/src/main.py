from src.utils.input_validator import get_valid_input
from src.game_logic.number_generator import generate_random_number
from src.game_logic.hint_generator import provide_hint


def main():
    score = 100
    actual_number = generate_random_number(1, 100)
    while True:
        user_input = get_valid_input(1, 100)
        if user_input == actual_number:
            print("hurray! You Win!")
            print(f"your score is {score}")
            break
        else:
            hint = provide_hint(user_input, actual_number)
            score -= 10
            score = max(score, 0)





if __name__== '__main__':
    main()