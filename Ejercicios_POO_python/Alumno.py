from ast import alias
from re import A


class Alumno():
    def inicializar(self, name, grade):
        self.name = name
        self.grade = grade

    def is_regular(self):
        if (self.grade >= 6):
            print(f"{self.name} esta aprobado con un {self.grade}")
        else:
            print(f"{self.name} esta desaprobado con un {self.grade}")

alumno1 = Alumno()
alumno1.inicializar("Mateo", 9)
alumno1.is_regular()

alumno2 = Alumno()
alumno2.inicializar("Elvio", 5)
alumno2.is_regular()
