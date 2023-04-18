random_matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]
min_value_rows = []
min_index_rows = []
max_value_rows = []
max_index_rows = []
for row in random_matrix:
    min_index = 0
    min_value = row[min_index]
    max_index = 0
    max_value = row[max_index]
    for index_col in range(len(row)):
        if row[index_col] < min_value:
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)
print("Minimal elements:", min_value_rows)  # минимальные элементы
print("Their indices:", min_index_rows)  # их индексы
print("Maximal elements:", max_value_rows)  # максимальные элементы
print("Their indices:", max_index_rows)  # их индексы
