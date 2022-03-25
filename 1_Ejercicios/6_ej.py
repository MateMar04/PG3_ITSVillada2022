phrase: str = input("Ingrese una frase: ")


def count_vowels(phrase: str):
    vowels: int = 0
    for i in phrase:
        if i in 'aeiouAEIOU':
            vowels += 1
    return vowels


print("En la frase hay " + str(count_vowels(phrase)) + " vocales")
