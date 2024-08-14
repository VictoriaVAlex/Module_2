my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    if my_list[index] == 0:
        index += 1  # переходим к следующем индексу, если текущий элемент равеен 0
        continue  # пропускаем остальные действия в текущей итерации
    if my_list[index] < 0:
        break
    print(my_list[index])
    index += 1
