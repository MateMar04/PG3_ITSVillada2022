def ask_number():
    try:
        number = int(input("Ingrese un numero: "))
        return number
    except ValueError:
        print("Error: No es un numero")
        return ask_number()


def get_result(last_result, number):
    last_result += number
    return last_result


number1 = ask_number()
number2 = ask_number()
result = get_result(number1, number2)
print(f"El resultado es: {result}")

continue_flag = True

while continue_flag:
    option = input("Desea continuar? (y/n): ")
    if option == "y":
        number = ask_number()
        result = get_result(result, number)
        print(f"El resultado es: {result}")
    elif option == "n":
        print("Adios!")
        continue_flag = False
    else:
        print("Error, ingrese una opcion valida")
