#Cree un programa que le pida al usuario ingresar 
#5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras

words = []
new_list = []

for i in range(5):
    user_words=input(f"Ingrese la palabra {i+1}: ")
    words.append(user_words)

for word in words:
    if len(word) > 4:
        new_list.append(word)

print(new_list)
