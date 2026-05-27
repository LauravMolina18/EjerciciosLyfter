#Cree un programa que muestre el valor más pequeño de una lista sin usar 

my_list = [4, 7, 5, 2, 3]

smallest = my_list[0]

for numbers in my_list:
    if numbers < smallest:
        smallest = numbers

print(f'El número más pequeño es: {smallest}')
    