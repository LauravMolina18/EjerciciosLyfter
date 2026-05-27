#Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string

def upper_lower_numbers(my_string):

    upper = 0
    lower = 0

    for i in range(len(my_string)):
        if my_string[i].isupper():
            upper = upper + 1 
        elif my_string[i].islower():
            lower = lower + 1 

    return upper, lower


upper, lower = upper_lower_numbers("I Have One Dog And His Name Is Zeus")
print(f"There is {upper} upper cases and {lower} lower cases")