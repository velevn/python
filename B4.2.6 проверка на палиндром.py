def fun(num):
    num = num.replace(' ', '')
    num = num.lower()
    num_str = ''.join(reversed(num))
    num_str = num_str.replace(' ', '')
    num_str = num_str.lower()
    if str(num) == num_str:
        return True
    else:
        return False


print(fun("Кит на море не романтик"))
