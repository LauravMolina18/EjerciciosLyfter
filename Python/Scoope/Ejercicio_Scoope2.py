#Intente acceder a una variable definida dentro de una función desde afuera.


def my_name():
    name = "laura"

my_name()
#print(name) da error

def my_name():
    name = "laura"
    return name

name = my_name()
print(name)


#Intente acceder a una variable global desde una función y cambiar su valor
#con global

my_age = 26

def change_age():
    global my_age
    my_age = my_age + 5

change_age()
print(my_age)


#con return

my_age = 26

def change_age_ret():
    return my_age + 5 

my_age = change_age_ret()
print(my_age)
