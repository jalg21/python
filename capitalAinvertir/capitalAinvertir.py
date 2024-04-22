#funcion
def calcular_capital(cantidad, interes, años):
    capital = cantidad #declarar la cantidad de inversion
  
    for i in range(1, años + 1): #arreglo para desplegar los años ingresados
        capital += capital * (interes / 100) #operacion para calcular el capital de cada año
        #imprimir resultado
        print("Capital tras", i, "años:", capital)

#solicitar inversion
cantidad = float(input("¿Cantidad a invertir?: "))
interes = float(input("¿Interés porcentual anual?: "))
años = int(input("¿Años?: "))

calcular_capital(cantidad, interes, años)