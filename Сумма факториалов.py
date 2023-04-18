n = int(input())
m = 1
c = 0
for i in range(1, n+1):
    m = i * m
    c = c + m
print(c)
