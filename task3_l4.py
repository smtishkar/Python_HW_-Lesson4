# 3'. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

from random import randint

# 1ый способ используем set

# lenght = int(input("Введите желаемое количество значений в списке: "))
# list = [randint(0,5) for i in range(lenght)]
# print(set(list))

# 2ой способ. Создание второго списка с уникальными значениями 

lenght = int(input("Введите желаемое количество значений в списке: "))
list = [randint(0,5) for i in range(lenght)]
list2 =[]
for i in range (lenght):
    if list[i] not in list2:
        list2.append(list[i])
print(list)
print(list2)
