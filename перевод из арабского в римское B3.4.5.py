ar_to_rm = [('M', 1000), ('CM', 900), ('D', 500),
            ('CD', 400), ('C', 100), ('LC', 90),
            ('L', 50), ('XL', 40), ('X', 10), ('IX', 9),
            ('V', 5), ('IV', 4), ('I', 1)]
n = input()

while int(n) > 0:
    rim = ''
    for i, j in ar_to_rm:
        while int(n) >= int(j):
            rim = rim + i
            n = int(n) - int(j)
print(rim)
