# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from unittest import result


path = '/Users/mac/python/seminar_04/DZ/file.txt'
f1 = open('file.txt', 'r')
f2 = open('file_2.txt', 'r')
f3 = open('summ.txt', 'w')
line1 = int(f1.readline())
line2 = int(f2.readline())
resultt = line1 + line2
f3.writelines(f'{resultt}')
f1,f2,f3.close()
print(resultt)
exit()


# l = [line.strip() for line in f]
# file = []
# l = ''.join(l)

# result = [int(item) for item in l]

# print(result)
# print(l)
# data = f.read()
# f.close()
# numbers = []
# while data != '':
#     space_pos = data.index('')
#     numbers.append(int(data))
#     data = data[space_pos+1:]
# out = []
# # for e in numbers:
# #     if not e % 2:
# #          out.append((e,e **2))
# print(out)


