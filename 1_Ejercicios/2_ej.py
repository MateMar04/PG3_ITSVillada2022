def is_biciesto(year: int):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("El año " + str(year) + " es bisiesto")
    else:
        print("El año " + str(year) + " no es bisiesto")


year: int = int(input("Ingrese un año: "))

is_biciesto(year)
