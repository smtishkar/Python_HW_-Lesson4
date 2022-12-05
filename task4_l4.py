# 4'. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0

from random import randint
k = int(input('Введите какой степени вы хотели бы составить многочлен: '))


iteration = k
a = 0

for i in range (iteration+1):
    if i == 0:
        a = str(a)
        a = f"{randint(0,100)}*x^{k} + "
        k = k-1         
    elif i < iteration and i !=0 and i != iteration:
        a += f"{randint(0,100)}*x^{k} + "
        k = k-1
    elif i == iteration:
        a += f"{randint(0,100)}*x + "
        k = k-1 
    if i == iteration:
        a += f"{randint(0,100)}"
        k = k-1
print(a)

with open ('file1.txt', 'w') as data:
    data.write(a)



