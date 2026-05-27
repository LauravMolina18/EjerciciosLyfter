#Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.

def my_string(my_words):

    word_list = my_words.split("-")
    word_list.sort()

    new_words = "-".join(word_list)
    return new_words

my_words = "laura-felipe-zeus"
result = my_string(my_words)
print(result)