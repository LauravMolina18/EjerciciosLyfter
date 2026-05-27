#Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto

def count_character(my_text, my_character): 

    character_times = 0

    for character in my_text:
        if character == my_character:
              character_times = character_times + 1

    return character_times


my_text = str(input("Ingrese un texto: " ))
my_character = str(input("Ingrese el caracter que desea buscar: "))
result = count_character(my_text, my_character)
print(f'El carácter "{my_character}" aparece {result} veces')