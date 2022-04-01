def is_palindrome(word: str):
    if word == word[::-1]:
        return True
    else:
        return False


word: str = input("Ingrese una palabra: ")

is_palindrome(word)

if is_palindrome:
    print("La palabra " + word + " es un palindromo")
else:
    print("La palabra " + word + " no es un palindromo")
