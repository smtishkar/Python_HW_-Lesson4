# 5'. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9


with open ('task5-1.txt', 'r') as data:
    initial_for_list1 = data.read()

with open ('task5-2.txt', 'r') as data:
    initial_for_list2 = data.read()

list1 = initial_for_list1.split(' + ')
list2 = initial_for_list2.split(' + ')

list1 = [i[0] for i in list1]
for i in range (len(list1)):
    if list1[i] == 'x':
        list1[i] = '1'

list2 = [i[0] for i in list2]
for i in range (len(list2)):
    if list2[i] == 'x':
        list2[i] = '1'

list1 = list(map(int,list1))
list2 = list(map(int,list2))

c = list(map(sum, zip(list1 + [0, ] * (x := len(list2) - len(list1)), list2 + [0, ] * -x)))

print(initial_for_list1)
print(initial_for_list2)
print('-' * 30)
print (f'{c[0]} * x ** 3 + {c[1]} * x + {c[2]}')
