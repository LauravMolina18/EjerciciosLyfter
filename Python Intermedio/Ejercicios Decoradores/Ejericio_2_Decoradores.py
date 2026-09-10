#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

def numbers_only(func):
    def wrapper(*args, **kwargs):
        for parameter in args:
            if not isinstance(parameter, (int, float)):
                raise ValueError("All parameters must be numbers")

        for parameter in kwargs.values():
            if not isinstance(parameter, (int, float)):
                raise ValueError("All parameters must be numbers")

        return func(*args, **kwargs)

    return wrapper


@numbers_only
def add_numbers(a, b):
    return a + b


print(add_numbers(5, 3))
