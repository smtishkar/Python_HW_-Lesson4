# 1'. Вычислить число Пи c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  

import numpy

# 1ый способ. значение указываем в формате 0.001 и в конце используем округление

# def float_accuracy_calc ():
#     count = 0
#     d = float(input('Введите точност числа Пи (в формате 0.001): '))
#     if d > 1:
#         print ("значение введено в некорректном формате")
#     else:
#         while d < 1:
#             d = d * 10
#             count += 1
#         return round(numpy.pi,count)

# 2ой способ, когда мы просто указываем точность цифрой
# rest = int(input('Введите точност числа Пи (количество знаков после запятой): '))
# print (round(numpy.pi,rest))



# 3ий способ. Почти как первый, но без округления 
def float_accuracy_calc2 ():
    count = 2
    d = float(input('Введите точност числа Пи (в формате 0.001): '))
    if d > 1:
        print ("значение введено в некорректном формате")
    else:
        while d < 1:
            d = d * 10
            count += 1
            a = str(numpy.pi)
        return (a[0:count])

print(float_accuracy_calc2())
