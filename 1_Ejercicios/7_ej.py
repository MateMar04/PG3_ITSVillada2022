number = int(input("Ingrese un numero: "))


def convert_to_list(number):
    list = []
    str_number = str(number)
    for i in range(len(str_number)):
        list.append(int(str_number[i]))
    return list


def is_step(list):
    for i in range(len(list)):
        if(list[i] == list[i+1] + 1 or list[i] == list[i+1] - 1):
            return True
        else:
            return False


if(is_step(convert_to_list(number))):
    print("El numero " + str(number) + " es un numero step")
else:
    print("El numero " + str(number) + " no es un numero step")
