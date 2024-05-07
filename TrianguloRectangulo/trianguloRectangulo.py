def imprimirtriangulo(altura): #Esta línea define una función llamada imprimir_triangulo_rectangulo que toma un parámetro llamado altura. Esta función imprimirá un triángulo rectángulo de asteriscos.
    for i in range(1, altura + 1):     #bucle for que itera sobre un rango de números desde 1 hasta altura, ambos inclusive. En cada iteración, i tomará un valor del rango.
        print('*' * i) #Dentro del bucle, esta línea imprime una cadena de asteriscos  multiplicada por el valor actual de i.

altura = int(input("Altura: ")) # Esta línea solicita al usuario que ingrese la altura deseada para el triángulo rectángulo y guarda el valor ingresado en la variable altura
imprimirtriangulo(altura) #imprimir resultado