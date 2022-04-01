from typing import List

list: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
searching: int = int(input("Ingrese un numero para buscar: "))


def search(list: List[int], searching: int):
    for i in range(len(list)):
        if list[i] == searching:
            print(f"El numero {searching} se encuentra en la posicion {i}")
            break
    else:
        print(f"El numero {searching} no se encuentra en la lista")


search(list, searching)
