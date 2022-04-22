class Operaciones:
    def __init__(self):
        self.number1 = int(input("Ingrese un numero: "))
        self.number2 = int(input("Ingrese otro numero: "))
        print(f"La suma entre {self.number1} y {self.number2} es {self.sum()}")
        print(f"La resta entre {self.number1} y {self.number2} es {self.subs()}")
        print(f"La multiplicacion entre {self.number1} y {self.number2} es {self.mult()}")
        print(f"La division entre {self.number1} y {self.number2} es {self.div()}")

    def sum(self):
        return self.number1 + self.number2

    def subs(self):
        return self.number1 - self.number2

    def mult(self):
        return self.number1 * self.number2

    def div(self):
        if (self.number2 == 0):
            return "DIVISION POR CERO NO POSIBLE"
        return self.number1 / self.number2


operaciones1 = Operaciones()
