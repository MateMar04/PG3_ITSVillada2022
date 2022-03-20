phrase = input("Ingrese una frase: ")


def count_vowels(phrase):
    vowels = 0
    for i in phrase:
        if i in 'aeiouAEIOU':
            vowels += 1
    return vowels


print("En la frase hay " + str(count_vowels(phrase)) + " vocales")
