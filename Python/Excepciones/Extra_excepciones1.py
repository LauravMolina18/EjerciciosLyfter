def name():
    try:
        user_name=str(input("Ingrese su nombre: "))

        if user_name.isdigit():
            raise ValueError

    except ValueError:
        print("El nombre no puede ser un número ")
        

name()

