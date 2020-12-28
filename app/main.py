
"""

In this we are to create an app that will be used to check our knowledge of square colors of the chessboard.


"""
import random

def get_y_or_n():
    value = input("Leave empty if white, enter anything for black:")
    if value == "":
        return True
    else:
        return False


def generate_set_of_squares():
    result = []
    is_white = True
    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        is_white = not is_white
        for number in range(1, 9):
            square = (letter, number)
            item = (square, is_white)
            result.append(item)
            is_white = not is_white
    return result

def main():
    all_squares = generate_set_of_squares()
    result_to_text = {True: "WHITE", False: "BLACK"}
    user_outcome_to_text = {True: "WIN!", False: "FAIL!"}
    while True:
        square, is_white = random.choice(all_squares)
        string_square = square[0] + str(square[1])
        print(string_square)
        user_is_white = get_y_or_n()
        print(f"{user_outcome_to_text[user_is_white==is_white]} The square {string_square} is {result_to_text[is_white]}")


if __name__ == "__main__":
    main()