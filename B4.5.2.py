def decorator_count(fn):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        fn(*args, **kwargs)
        count += 1
        print(f'Функция {fn} была вызвана {count} раз.')
    return wrapper


@decorator_count
def my_kv():
    print(10 ** 2)


my_kv()
my_kv()
my_kv()
