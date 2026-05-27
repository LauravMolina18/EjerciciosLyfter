secret_number = 8 
user_number=int(input("Ingrese el número que cree que será el correcto: "))
while user_number != secret_number:
    print ("Intente de nuevo")
    user_number=int(input("Ingrese el número que cree que será el correcto: "))
print("Felicitaciones adivinaste!")