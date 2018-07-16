#Дан массив чисел.
#[10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

#4.1) убрать из него повторяющиеся элементы
#4.2) вывести 3 наибольших числа из исходного массива
#4.3) вывести индекс минимального элемента массива
#4.4) вывести исходный массив в обратном порядке

def remove_repeat_elem(lst):
    without_repeat_lst = []
    for i in lst:
        if i not in without_repeat_lst:
            without_repeat_lst.append(i)
    return without_repeat_lst

print(remove_repeat_elem([10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]))


def get_three_max_numbers(lst):
     a = sorted(lst, reverse = True) [0 : 3]
     return a
print(get_three_max_numbers([10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]))


def min_index(lst):
    return lst.index(min(lst))
print(min_index([10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]))


def list_reverse(lst):
    return lst[::-1]
print(list_reverse([10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]))







