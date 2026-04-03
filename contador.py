import random

print("Bienvenido al contador de números aleatorios.")

def numero_aleatorio():
    return random.randint(1, 100)


def contador():
    while True:
        dificultad = input("Selecciona la dificultad (facil, medio, dificil): ").lower()
        if dificultad == "facil":
            return 10
        elif dificultad == "medio":
            return 5
        elif dificultad == "dificil":
            return 3
        else:
            print("Dificultad no válida. Se establecerá en 'medio' por defecto.")
            return 5

  
def comparar (ingrese_numero, numero):
    if ingrese_numero == numero:
        print(f"¡Felicidades! Has adivinado el número. {numero} es el número correcto.")
        return True
    elif  ingrese_numero < numero:
            print("El número es mayor que el que ingresaste.")
    else:
        print("El número es menor que el que ingresaste.")

    

def main():
    print("¡Vamos a jugar! Estoy pensando en un número entre 1 y 100.")
    numero = numero_aleatorio()
    oportunidades = contador()

    while oportunidades >0:
        try:
            ingrese_numero = int(input(f"Ingresa tu número ({oportunidades} oportunidades restantes): "))
            if comparar(ingrese_numero, numero):
                break
            oportunidades -= 1
        except ValueError:
            print("Por favor, ingresa un número válido.")
       

    else:
        print(f"Lo siento, has agotado tus oportunidades. El número correcto era {numero}.")

if __name__ == "__main__":
    main()