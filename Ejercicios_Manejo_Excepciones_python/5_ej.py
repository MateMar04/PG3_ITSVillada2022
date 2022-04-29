text = input("Ingrese un texto: ")

try:
    file = open("demofile.txt", "a")
    file.write(text)
    file.close()
except TypeError:
    print("Error, no se puede escribir un int")
