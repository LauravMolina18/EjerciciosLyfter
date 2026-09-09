#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

def numbers_only(func):
    def wrapper(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("All parameters must be numbers")

        return func(a, b)

    return wrapper


@numbers_only
def add_numbers(a, b):
    return a + b


print(add_numbers(5, 3))