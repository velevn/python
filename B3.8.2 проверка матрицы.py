matrix = [[1, 2, 3],
          [7, -1, 2],
          [123, 2, -1],
          [2, 2, 2]
          ]

col_row = 0
col_elem = 0

for row in range(len(matrix)):
    col_row = row
    for elem in range(len(matrix[row])):
        col_elem = elem
if col_row == col_elem:
    print(True)
else:
    print(False)
