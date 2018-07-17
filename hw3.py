#Заменить в произвольной строке согласные буквы на гласные.

import random
def consonant_line(str):
    CONSONANT_LETTERS = ["A", "E", "I", "O", "U", "Y"]
    VOVEL_LETTERS = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N","P", "Q", "R", "S", "T", "V", "W", "X", "Y",
                     "Z"]
    consonant_list = []
    consonant_str = ''

    for char in str:
        if char.upper() in CONSONANT_LETTERS:
            char = VOVEL_LETTERS[random.randint(0, len(VOVEL_LETTERS) - 1)].lower()
        consonant_list.append(char)
        consonant_str = ''.join(consonant_list)
    return consonant_str

print(consonant_line('Python is an interpreted high-level programming language for general-purpose programming'))
