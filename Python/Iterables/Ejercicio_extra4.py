#Cree un programa que reciba una lista de números y calcule el promedio de los valores
#luego cree una nueva lista con solo los valores mayores al promedio

numbers = []
new_list = []
total = 0

for i in range(5):
    user_numbers = int(input(f"Ingrese el número {i+1}: "))
    numbers.append(user_numbers)

for number in numbers:
    total = total+number

average = total / len(numbers)

for num in numbers:
    if num > average:
        new_list.append(number)

print(f'Promedio: {average}\nNueva lista: {new_list}')

