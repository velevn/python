matrix = [[1, 2, 3],
          [7, -1, 2],
          [123, 2, -1]
          ]

max_value_rows = []

for row in matrix:
    max_index = 0
    max_value = row[max_index]
    for index_col in range(len(row)):
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
    max_value_rows.append(max_value)

print("Maximal element:", max(max_value_rows))  # максимальные элементы
