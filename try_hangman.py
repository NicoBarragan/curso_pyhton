import random
import os


def normalize(text): # It removes the accents of a string
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        )
    for a, b in replacements:
        text = (text.replace(a, b))
    text = text.upper().strip()
    return text

def read_data(filepath):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(normalize(line))
    return words

def run():
    word_list = read_data(filepath="./archivos/data.txt")

    word = random.choice(word_list)
    word_letter_list = [letter for letter in word]
    word_underscores_list = ["_"] * len(word_letter_list)
    letter_index = {}
    
    for idx, letter in enumerate(word):
        if not letter_index.get(letter): 
            letter_index[letter] = []
        letter_index[letter].append(idx)
    
    while True:
        os.system("clear") # Si estás en Windows cambia clear por cls
        print("¡Adivina la palabra!")
        for element in word_underscores_list:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in word_letter_list:
            for idx in letter_index[letter]:
                word_underscores_list[idx] = letter
        
        if "_" not in word_underscores_list:
            os.system("clear") # Si estás en Unix (Mac o Linux) cambia cls por clear
            print("¡Ganaste! La palabra era", word)
            break


if __name__ == '__main__':
    run()
    
# def clean_data(word_list):
#     tildes = {'Á':'A', 'É':'E', 'Í':'I', 'Ó':'O', 'Ú':'U'}

#     new_list = []
#     for word in word_list:
#         for key, value in tildes.items():
#             if key in word:
#                 new_word = word.replace(key, value)
#                 new_list.append(new_word)
#             elif key not in word:
#                 new_list.append(word)

#     print(new_list)


#     clean_data(read_data(filepath="./archivos/test_archives.txt"))
                    
                    
#                     # #word[i] = word[i].replace(key, value)
                    

# import random
# import os

# def run():
#     data = read_data(filepath="./archivos/data.txt")
#     chosen_word = random.choice(data)
#     chosen_word_list = [letter for letter in chosen_word]
#     chosen_word_list_underscores = ["_"] * len(chosen_word_list)
#     letter_index_dict = {}
#     for idx, letter in enumerate(chosen_word):
#         if not letter_index_dict.get(letter): 
#             letter_index_dict[letter] = []
#         letter_index_dict[letter].append(idx)
    
#     while True:
#         os.system("clear") # Si estás en Unix (Mac o Linux) cambia cls por clear
#         print("¡Adivina la palabra!")
#         for element in chosen_word_list_underscores:
#             print(element + " ", end="")
#         print("\n")

#         letter = input("Ingresa una letra: ").strip().upper()
#         assert letter.isalpha(), "Solo puedes ingresar letras"

#         if letter in chosen_word_list:
#             for idx in letter_index_dict[letter]:
#                 chosen_word_list_underscores[idx] = letter
        
#         if "_" not in chosen_word_list_underscores:
#             #os.system("clear") # Si estás en Unix (Mac o Linux) cambia cls por clear
#             print("¡Ganaste! La palabra era", chosen_word)
#             break


# if __name__ == '__main__':
#     run()