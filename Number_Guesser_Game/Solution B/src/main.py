from src.utils.input_validator import get_valid_input


def main():
    user_input = get_valid_input(1, 100)
    print(user_input)


if __name__== '__main__':
    main()