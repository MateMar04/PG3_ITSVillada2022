def draw(height: int, wide: int, caracter: str):
    for i in range(height):
        for j in range(wide):
            print(caracter, end="")
        print()


wide: int = int(input("Ingrese el ancho del rectangulo: "))
height: int = int(input("Ingrese el alto del rectangulo: "))
caracter: str = input("Ingrese el caracter que desea usar: ")

draw(height, wide, caracter)
