def is_biciesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        print("El año " + str(anio) + " es bisiesto")
    else:
        print("El año " + str(anio) + " no es bisiesto")


anio = int(input("Ingrese un año: "))

is_biciesto(anio)
