import random


def Number_guess(x):
    if x > 10:
        print(f"{x} is an invalid input")
    else:
        int_list = [int(char) for char in str(x*9)]
        print(f'Input: {x}, Output: {sum(int_list)+4}')


Number_guess(random.randint(1, 14))
Number_guess(random.randint(1, 14))
Number_guess(random.randint(1, 14))
Number_guess(random.randint(1, 14))
