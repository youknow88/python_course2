#1)	Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).
#keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#ожидаемый результат: {1: 1, 2: 4, 3: 9 …}


keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def generate_dict(keys):
    key_dict = dict()
    keys_list_length = (len(keys)) + 1
    for key in range(keys[0], keys_list_length):
        key_dict[key] = key * key
    print(key_dict)


generate_dict(keys)