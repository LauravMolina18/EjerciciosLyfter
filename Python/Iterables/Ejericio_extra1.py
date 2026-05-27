#Cree un programa que cuente cuántas veces aparece un número específico en una lista.
#Pida al usuario una lista de números y otro número a buscar

user_numbers=int(input("Cuántos números desea ingresar?: "))
search_number=int(input("Ingrese el número específico que desea buscar: "))

list_numbers=[]

for i in range(user_numbers):
    numbers=int(input("Ingrese un número: "))
    list_numbers.append(numbers)

counter = 0 

for number in list_numbers:
    if number == search_number:
        counter = counter+1

print(f'El número {search_number} aparece {counter} veces')


