def multi(*nums):
    result = 1
    for n in nums:
        result = result * n
    return result


print(multi(4, 6, 54, 23))
