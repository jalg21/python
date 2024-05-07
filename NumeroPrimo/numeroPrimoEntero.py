pyramid = int(input("Introduce un numero: ")) #Esta línea solicita al usuario que ingrese un número y guarda el valor ingresado en la variable pyramid
for height in range(1, pyramid+1, 2): # Este bucle for itera sobre los números impares desde 1 hasta el número ingresado (pyramid) inclusive. 
    for number in range(height, 0, -2):
        print(number, end=" ")
    print("")