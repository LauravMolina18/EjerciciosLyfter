#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

numbers=[]
highest_number=0

for index in range(10):
    user_numbers =int(input("Ingrese un número: "))
    numbers.append(user_numbers)

    if user_numbers > highest_number:
        highest_number=user_numbers

print(numbers)
print(f'El más alto fue: {highest_number}')


