#Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def show_info(func):
    def wrapper(*args, **kwargs):
        print("Parameters:", args, kwargs)

        result = func(*args, **kwargs)

        print("Return:", result)

        return result

    return wrapper


@show_info
def add_numbers(a, b):
    return a + b


print(add_numbers(5, 3))

