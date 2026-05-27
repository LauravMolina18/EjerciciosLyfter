#Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

list_one=['Amarillo', 'verde', 'morado', 'azul']
list_two=['rosa', 'negro', 'rojo', 'dorado']

for index in range(len(list_one)):
    first=list_one[index]
    second=list_two[index]
    print(first, second)