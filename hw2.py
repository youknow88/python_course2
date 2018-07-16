#Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.
import random

for i in range(random.randint(1, 100)):
    even_list = []
    if i % 2 == 0:
        even_list.append(i)
        print(even_list)


