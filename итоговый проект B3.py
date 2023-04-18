def fun(x):
    first_digit = x // 10
    second_digit = x % 10
    return (first_digit == 5) or (second_digit == 5) or (first_digit == 7) or (second_digit == 7) or (first_digit == 9) or (second_digit == 9)


print(fun(769))
