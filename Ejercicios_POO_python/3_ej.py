class Triangulo:
    def inicializar(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.sides = [side1, side2, side3]

    def is_equilatero(self):
        if (self.side1 == self.side2 == self.side3):
            print("El triangulo es EQUILATERO")
        else:
            print("El triangulo NO ES EQUILATERO")
            self.find_biggest_side()

    def find_biggest_side(self):
        for i in range(len(self.sides)):
            biggest = self.sides[1]
            if (self.sides[i] > biggest):
                biggest = self.sides[i]
        print(f"El lado mayor del triangulo es {biggest}")


triangulo1 = Triangulo()
triangulo1.inicializar(1, 2, 3)
triangulo1.is_equilatero()

triangulo2 = Triangulo()
triangulo2.inicializar(2, 2, 2)
triangulo2.is_equilatero()
