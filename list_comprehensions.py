def main():
    # lista = []
    # i = 0
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         lista.append(i**2)
    
    # lista = [i**2 for i in range(1, 101) if i % 3 != 0] 
    # print(lista)

    list = [i for i in range(1, 10001) if i % 4 == 0 and 
    i % 6 == 0 and i % 9 == 0]

    print(list)

def run():
    print('-'*50)
    lista = [1, 2, 3, 4, 5]
    map = [i**2 for i in lista]
    print(map)

if __name__ == '__main__':
    main()
    run()