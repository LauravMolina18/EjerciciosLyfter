#Cree una función que reciba un string y retorne cuántas vocales contiene

def my_vowel(my_string):

    counter = 0

    for vowel in my_string:
        if vowel  in "aeiouAEIOU":
            counter = counter + 1
    
    return counter


my_string = str(input("Ingrese una palabra: "))
result = my_vowel(my_string)
print(result)