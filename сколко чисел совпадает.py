n = int(input())
n1 = int(input())
n2 = int(input())

if n == n1 == n2:
    print(3)
elif n == n1 or n == n2 or n1 == n2:
    print(2)
else:
    print(0)
