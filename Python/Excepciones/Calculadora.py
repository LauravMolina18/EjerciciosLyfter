def calculator():
    actual_number = 0

    while True:
        try:
            option = int(input("""
Seleccione una opción:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar
6. Salir
                   
Opción:              
"""))
        
            if option < 1 or option > 6:
                print("Opción inválida")
                continue
            if option == 6:
                print("Cerrando calculadora...")
                break
            if option !=5:
                user_number = int(input("Ingrese el número con el que va a realizar la operación: "))

            if option == 1:
                actual_number =actual_number + user_number
            elif option == 2:
                actual_number = actual_number - user_number
            elif option == 3:
                actual_number = actual_number * user_number
            elif option == 4:
                if user_number == 0:
                    print("No se puede dividir por 0")
                    continue
                actual_number =actual_number / user_number
            elif option == 5:
                actual_number = 0

            print(f"Resultado: {actual_number}")

        except ValueError:
            print("Ingrese un número válido: ")

calculator()

