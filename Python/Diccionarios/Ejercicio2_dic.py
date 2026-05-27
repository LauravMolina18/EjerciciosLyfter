#Cree un programa que cree un diccionario usando dos 
#listas del mismo tamaño, usando una para sus keys, y la otra para sus values.

first_list = ['color', 'brand', 'type', 'name']
second_list = ['blue', 'adidas', 'shoes', 'vanessa']

new_dict = {}

for i in range(len(first_list)):
    new_dict[first_list[i]] = second_list[i]

print(new_dict)