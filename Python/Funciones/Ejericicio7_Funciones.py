#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def prime_numbers(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

def numbers_list(my_list):
    new_list = []

    for numbers in my_list:
        if prime_numbers(numbers):
            new_list.append(numbers)

    return new_list



my_list = [1, 2, 3, 6, 5, 10, 12]

result = numbers_list(my_list)
print(result)