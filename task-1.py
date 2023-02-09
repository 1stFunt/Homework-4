# Даны два неупорядоченных набора целых чисел (может быть, сповторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.

n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))
list_1 = list()
list_2 = list()
for i in range(n):
    list_1.append(int(input()))
for i in range(m):
    list_2.append(int(input()))
print(*list_1)
print(*list_2)
list_1 = set(list_1)
list_2 = set(list_2)
List_i = list_1.intersection(list_2)
print(*List_i)