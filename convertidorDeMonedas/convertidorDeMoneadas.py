def convertir_a_monedas(cantidad):
    # Inicializar las variables para contar las monedas
    monedas_20 = 0
    monedas_10 = 0
    monedas_5 = 0
    monedas_1 = 0
    
    # Calcular las  monedas de $20
    monedas_20 = cantidad // 20
    cantidad %= 20
    
    #el % es para que se pueda obetener el valor restante despues de restar todas las monedas de 20
    monedas_10 = cantidad // 10
    cantidad %= 10
    
    # Calcular las monedas de $5
    monedas_5 = cantidad // 5
    cantidad %= 5
    
    # calcular las monedas de $1 con lo que sobre
    monedas_1 = cantidad
    
    # Imprimir resultado
    print("Monedas de $20:", monedas_20)
    print("Monedas de $10:", monedas_10)
    print("Monedas de $5:", monedas_5)
    print("Monedas de $1:", monedas_1)

# Solicitar cantidad de monedas
cantidad = int(input("Cantidad a Convertir: "))

# Llamar a la funcion
convertir_a_monedas(cantidad)