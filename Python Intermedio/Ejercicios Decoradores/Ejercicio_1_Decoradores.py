#Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def show_info(func):
    def wrapper(a, b):
        print("Parameters:", a, b)

        result = func(a, b)

        print("Return:", result)

        return result

    return wrapper


@show_info
def add_numbers(a, b):
    return a + b


print(add_numbers(5, 3))