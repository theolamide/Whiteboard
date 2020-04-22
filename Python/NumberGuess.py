def Number_guess(x):
    if x > 10:
        print(f"{x} is an invalid input")
    else:
        b = [int(char) for char in str(x*9)]
        print(f'Input: {x}, Output: {sum(b)+4}')


Number_guess(4)
Number_guess(5)
Number_guess(1)
Number_guess(12)
