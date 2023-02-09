# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input('Введите кол-во кустов на грядке: '))
list_1 = list()
for i in range(n):
    list_1.append(int(input()))
print(*list_1)
list_result = list()
for i in range(len(list_1)):
    if i <= len(list_1) - 2:
        list_result.append(list_1[i] + list_1[i + 1] + list_1[i - 1])
    else:
        list_result.append(list_1[i] + list_1[i - 1] + list_1[0])
print(max(list_result))   # max = 0
                          # for i in list_result:
                          #   if i > max:
                          #       max = i
                          # print(max) 