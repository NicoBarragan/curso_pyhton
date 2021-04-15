import random
import os
#   os.system('clear')

def juego():
    palabras = []
    with open('./data.txt', 'r') as f:
        for line in f:
            palabras.append(line.rstrip())

    seleccion = random.choice(palabras).upper()
    print(seleccion)

    guion = {idx:' _ ' for idx, char in enumerate(seleccion)}
    list = [' _ ' for idx, char in enumerate(guion)]
    print(list)
    d = ''
    print(guion)

    preg = input('Escribí una letra: ').upper() 
    h = list(map(lambda preg: char if preg == char, enumerate(seleccion))

    print(h)

    print(guion)
    print(d)


def main():
    juego()



if __name__ == '__main__':
    main()
    
    
    
    # dect = {idx:char for idx, char in enumerate(seleccion)}
    # long = len(seleccion)
    # guion = [' - ' for i in seleccion]
    # print(seleccion)
    # print('-'*50 )

    # dect_guion_list = {idx:' _ ' for idx,char in enumerate(seleccion)}
    

    # for i in range(len(intentos)):
    #     preg = input('Escribi una letra: ').upper()
    #     for idx, char in enumerate(seleccion):
    #         if preg == char:
    #             dect_guion_list[idx] = char
    #             intentos.append(1)
    #         else:
    #             continue

    #     os.system('clear')
        
    #     # dect_guion_list= {idx:char 
    #     # for idx,char in enumerate(seleccion) if char == preg}