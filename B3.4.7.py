# Введите свое решение ниже
def fun(A, B, C):
    if A < 45 and B > 45 and C > 45:
        return 'One of numbers is less than 45'
    elif B < 45 and A > 45 and C > 45:
        return 'One of numbers is less than 45'
    elif C < 45 and A > 45 and B > 45:
        return 'One of numbers is less than 45'
    else:
        return 'None of numbers is less than 45 or two numbers are less than 45'
