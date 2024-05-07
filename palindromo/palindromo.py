def es_palindromo(palabra):
    # Convertir la palabra a minúsculas para hacer la comparación sin importar mayúsculas o minúsculas
    palabra = palabra.lower()
    # Eliminar los espacios en blanco
    palabra = palabra.replace(" ", "")
    # Comparar la palabra original con su inversa
    return palabra == palabra[::-1]

palabra = input("Palabra: ")
if es_palindromo(palabra):
    print("La palabra sí es un palíndromo")
else:
    print("La palabra no es un palíndromo")