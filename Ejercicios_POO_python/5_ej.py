class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_data(self):
        print(f"{self.name}, {self.age} años")


class Empleado(Persona):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def print_data(self):
        print(f"{self.name}, {self.age} años, salario ${self.salary}")


continue_flag = True

while continue_flag:
    selection = int(input("1.Cargar Persona\n2.Cargar Empleado\n3.Salir\n"))
    if selection == 1:
        name = input("Ingrese el nombre de la persona: ")
        age = int(input("Ingrese la edad de la persona: "))
        persona = Persona(name, age)
        persona.print_data()
    elif selection == 2:
        name = input("Ingrese el nombre del empleado: ")
        age = int(input("Ingrese la edad del empleado: "))
        salary = int(input("Ingrese el salario del empleado: "))
        empleado = Empleado(name, age, salary)
        empleado.print_data()
    elif selection == 3:
        continue_flag = False
    else:
        print("Ingrese opccion correcta")

