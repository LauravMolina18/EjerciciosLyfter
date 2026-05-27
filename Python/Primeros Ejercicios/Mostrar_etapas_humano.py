#Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, 
#niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

name = input("Ingrese su nombre:")
last_name = input("Ingrese su apellido:")
age = int(input("Ingrese su edad:"))

if (age <= 4 ):
    print("Es un bebé")
elif (age >= 5 and age <=10):
    print("Es un niño")
elif(age >=11 and age <=14):
    print("Es un preadolescente")
elif(age >=15 and age <=20):
    print("Es un adolescente")
elif(age >=21 and age <=30):
    print("Es un adulto joven")
elif(age >=31 and age <=62):
    print("Es un adulto")
else:
    print("Es un adulto mayor")

