from pprint import pprint as pp
from itertools import groupby
#	Дан массив из словарей
data = [{'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
             {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
             {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
             {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
             {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
             {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

#6.1) отсортировать массив из словарей по значению ключа ‘age'
#6.2) сгруппировать данные по значению ключа 'city'
       #вывод должен быть такого вида :
       #{
          #‘Kiev’: [ {‘name’: ‘Viktor’, ‘age’: 30 },
                      # {‘name’: ‘Andrey’, ‘age’: 34}],
          #‘Dnepr’: [ {‘name’: ‘Maksim’, ‘age’: 20 },
                          #{‘name’: ‘Artem’, ‘age’: 50}],
         # ‘Lviv’: [ {‘name’: ‘Vladimir’, ‘age’: 32 },
                       #{‘name’: ‘Dmitriy’, ‘age’: 21}]

def sort_dict(data):
    sorted_list = (sorted(data, key=lambda k: k['age']))
    return sorted_list
pp(sort_dict([{'name': 'Viktor', 'city': 'Kiev', 'age': 30},
             {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
             {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
             {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
             {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
             {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]))