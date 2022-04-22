class Persona:
    def inicializar(self, name):
        self.name = name

    def print_name(self):
        print(f"Nombre: {self.name}")


persona1 = Persona()
persona1.inicializar("Mateo")
persona1.print_name()

persona2 = Persona()
persona2.inicializar("Elvio")
persona2.print_name()
