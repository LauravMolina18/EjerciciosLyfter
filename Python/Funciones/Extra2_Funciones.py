#Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras

def my_words(words, n):

    new_list = []

    for my_list in words:
        if len(my_list) > n:
            new_list.append(my_list)

    return new_list


words = ["Laura", "Vanessa", "Molina", "Luna"]
n = 5
result = my_words(words, n)
print(result)