n = int(input())
n1 = int(input())
n2 = int(input())

if n < n1 and n < n2:
    print(n)
elif n1 < n and n1 < n2:
    print(n1)
elif n2 < n and n2 < n1:
    print(n2)
