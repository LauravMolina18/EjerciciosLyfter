#Cree un algoritmo que muestre cuántos años tendrá usted dentro de 10 años

age = 26
future = 10
future_age = age + future
print ("Dentro de 10 años yo tendré", future_age, "años")

#Dado el nombre y apellido de un empleado, y el dominio .com de una empresa, genere 
# su email usando el formato <nombre>.<apellido>@<dominio_de_empresa>.com.

name = input("Enter your name:")
last_name = input("Enter your last name:")
domain = input("Enter your domain:")

print(f'{name}.{last_name}@{domain}.com')