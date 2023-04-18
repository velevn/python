def fun(num):
    num_str = ''.join(reversed(str(num)))
    if str(num) == num_str:
        return True
    else:
        return False


print(fun(445))
