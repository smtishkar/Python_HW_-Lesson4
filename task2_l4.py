# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

number = int(input('Введите число: '))
devider = 2
list = []

while devider **2 <= number:
    if number % devider == 0:
        list.append(devider)
        number //= devider
    else:
        devider += 1
if number != 1:
    list.append(number)
print(list)    #вывод всех простых множителей    
print(set(list))   #вывод уникальных простых множителей  
