#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.

import random
secret_number = random.randint(1, 10)

number=int(input("Ingrese el número que cree es el secreto:"))

while (secret_number != number):
    print("Intenta nuevamente")
    number=int(input("Ingrese el número que cree es el secreto:"))

print("Adivinaste!")