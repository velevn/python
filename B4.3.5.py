def sum_num(n):
    if n < 0:
        return n
    return n % 10 + sum_num(n // 10)


print(sum_num(0))
