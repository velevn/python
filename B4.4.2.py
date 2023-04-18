def fib(my_list):
    b = my_list
    while True:
        yield b
        b = b + my_list


for n in fib([1, 4, 6]):
    print(n)
