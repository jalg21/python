import random

def adivinar_numero_inverso():
    print("Bienvenido al juego de Adivinar el Número Inverso!")
    print("Piensa en un número entre 1 y 100, y yo trataré de adivinarlo.")
    print("Después de cada intento, dime si tu número es 'menor' o 'mayor'.")
    
    limite_inferior = 1
    limite_superior = 100
    
    while True:
        intento = random.randint(limite_inferior, limite_superior)
        print("¿Es {} tu número?".format(intento))
        respuesta = input("Indica si es 'menor', 'mayor', o 'si' si he acertado: ").lower()
        
        if respuesta == "menor":
            limite_superior = intento - 1
        elif respuesta == "mayor":
            limite_inferior = intento + 1
        elif respuesta == "si":
            print("¡Genial! He adivinado tu número.")
            break
        else:
            print("Respuesta no válida. Por favor, elige entre 'menor', 'mayor', o 'si'.")

if __name__ == "__main__":
    adivinar_numero_inverso()