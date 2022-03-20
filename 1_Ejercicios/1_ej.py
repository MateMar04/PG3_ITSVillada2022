lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def buscar(lista):
    search = int(input("Ingrese un numero para buscar "))
    for i in range(len(lista)):
        if (lista[i] == search):
            print("El numero " + str(search) + " esta en el indice " + str(i))


buscar(lista)
