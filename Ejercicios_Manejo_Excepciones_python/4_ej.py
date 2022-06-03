def ask_number():
    try:
        number = int(input("Ingrese un numero: "))
        return number
    except ValueError:
        print("Error: No es un numero")
        return ask_number()


def divide(dividend, divisor):
    try:
        division = dividend / divisor
        return division
    except ZeroDivisionError:
        return "Error: No se puede dividir entre 0"


number1 = ask_number()
number2 = ask_number()

print(divide(number1, number2))
