def draw_square(height: int, wide: int, caracter: str):
    for i in range(height):
        for j in range(wide):
            print(caracter, end="")
        print()


def draw_triangle(base: int, caracter: str):
    for i in range(base):
        espacios: int = base - (i + 1)
        print((" ") * espacios + (caracter + " ") * (i + 1))


wide_s: int = int(input("Ingrese el ancho del rectangulo: "))
height_s: int = int(input("Ingrese el alto del rectangulo: "))
caracter_s: str = input("Ingrese el caracter que desea usar: ")

draw_square(height_s, wide_s, caracter_s)

base_t: int = int(input("Ingrese la base del triangulo: "))
caracter_t: str = input("Ingrese el caracter que desea usar: ")

draw_triangle(base_t, caracter_t)
