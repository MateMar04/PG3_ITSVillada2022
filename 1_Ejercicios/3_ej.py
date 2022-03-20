def draw(height, wide, caracter):
    for i in range(height):
        for j in range(wide):
            print(caracter, end='')
        print()


wide = int(input("Ingrese el ancho del rectangulo: "))
height = int(input("Ingrese el alto del rectangulo: "))
caracter = input("Ingrese el caracter que desea usar: ")

draw(height, wide, caracter)
