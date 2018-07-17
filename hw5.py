#Найти общие ключи в двух словарях:

dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_two = {'a': 6, 'b': 7, 'z': 20, 'x': 40}




def same_keys_in_dicts(dict_one, dict_two):
    keys_dict1 = set(dict_one.keys())
    keys_dict2 = set(dict_two.keys())
    intersect_keys = keys_dict1.intersection(keys_dict2)
    return intersect_keys

print(same_keys_in_dicts({'a': 1, 'b': 2, 'c': 3, 'd': 4}, {'a': 6, 'b': 7, 'z': 20, 'x': 40}))