def fib(i=1, n=5):
    b = i
    while True:
        yield b
        b = b + n


for n in fib():
    print(n)
