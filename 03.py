# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

list_number = [1, 1, 2, 3, 4, 5, 5]

# result = []
# for i in range(0, len(list_number)):
#     if list_number[i] == list_number[i + 1]:
#         result.append(list_number[i])

# print(result)
list_number = [1, 1, 2, 3, 4, 5, 5, 4,7]
a = [int(i) for i in list_number]
for i in a:
    if a.count(i) == 1:
        print(i)
