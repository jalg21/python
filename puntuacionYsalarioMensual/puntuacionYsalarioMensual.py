# función 
def calcular_dinero(salario, puntuacion):
    # rendimiento según la puntuación
    nivel = ""
    if puntuacion >= 0 and puntuacion <= 3:
        nivel = "Inaceptable"
    elif puntuacion >= 4 and puntuacion <= 6:
        nivel = "Aceptable"
    elif puntuacion >= 7 and puntuacion <= 10:
        nivel = "Meritorio"
    else:
        return "Puntuación inválida"
    
    
    dinero = salario * (puntuacion / 10)
    
    return nivel, dinero

# solicitar datos-ingresar datos
salario = float(input("Ingrese su salario mensual: "))
puntuacion = int(input("Ingrese su puntuación en la evaluación: "))


nivel_rendimiento, cantidad_dinero = calcular_dinero(salario, puntuacion)

# Imprimir 
print("Nivel de Rendimiento:", nivel_rendimiento)
print("Cantidad de Dinero Recibido: ${:.2f}".format(cantidad_dinero))