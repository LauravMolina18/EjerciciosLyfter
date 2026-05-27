#Cree una función que le dé la vuelta a un string y lo retorne.

def my_string(my_word):

    reversed_word = ""

    for i in range(len(my_word) -1, -1, -1):
        reversed_word = reversed_word + my_word[i]
    return reversed_word


result = my_string('Hellow World')   
print(result)

