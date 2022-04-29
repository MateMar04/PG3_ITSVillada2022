def ask_number():
    try:
        number = int(input("Ingrese un numero de un mes: "))
        return number
    except ValueError:
        print("Error: No es un numero")
        return ask_number()


months = (
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Spetiembre", "Octubre", "Noviembre",
    "Diciembre")

selection = ask_number()
try:
    print(months[selection - 1])
except IndexError:
    print("El numero que se ingreso no corresponde a ningun mes")
