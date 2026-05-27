def show_menu():
    return int(input("""
Seleccione una opción:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar
6. Salir
                   
Opción:              
"""))

def add(current_number, user_number):
    return current_number + user_number

def subtract(current_number, user_number):
    return current_number - user_number

def multiply(current_number, user_number):
    return current_number * user_number

def divide(current_number, user_number):
    if user_number == 0:
        print("No se puede dividir por 0")
        return current_number
    return current_number / user_number

def clear():
    return 0

def main():
    current_number = 0

    while True:
        try:
            option = show_menu()

            if option < 1 or option > 6:
                print("Opción inválida")
                continue

            if option == 6:
                print("Cerrando calculadora...")
                break

            if option != 5:
                user_number = int(input("Ingrese el número con el que va a realizar la operación: "))

            if option == 1:
                current_number = add(current_number, user_number)
            elif option == 2:
                current_number = subtract(current_number, user_number)
            elif option == 3:
                current_number = multiply(current_number, user_number)
            elif option == 4:
                current_number = divide(current_number, user_number)
            elif option == 5:
                current_number = clear()

            print(f"Resultado: {current_number}")

        except ValueError:
            print("Ingrese un número válido")

main()