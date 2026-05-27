counter=1
result=0

user_number=int(input("Ingrese su número: "))
while (counter <= user_number):
    result=result+counter
    counter=counter+1
print(f"El resultado de la suma es: {result}")
