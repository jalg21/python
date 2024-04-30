
import random

#crear la lista aleatoria 
def listas(lst):
    n = len(lst)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]

# imprimir letras
letters = ['a', 'b', 'c']
print(f"letras: {letters}")

listas(letters)
print(f" Aleatorio: {letters}")












