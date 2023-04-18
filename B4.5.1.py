import time

N = 100


def decorator_time(fn):
    def wrapper():
        # print(f"Запустилась функция {fn}")
        t0 = time.time()
        # print(fn())
        dt = time.time() - t0
        # print(f"Функция выполнилась. Время: {dt:.10f}")
        return dt  # задекорированная функция будет возвращать время работы
    return wrapper


def pow_2():
    return 10000000 ** 2


def in_build_pow():
    return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

s_pow_2 = 0
s_in_build_pow = 0

for i in range(0, N):
    s_pow_2 += pow_2()
    s_in_build_pow += in_build_pow()

print(f"Функция выполнилась. Время: {(s_pow_2/N):.10f}")
print(f"Функция выполнилась. Время: {(s_in_build_pow/N):.10f}")
