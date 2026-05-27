print("Debe ingresar tres números, los tres deben ser diferentes")
number_one=int(input("Ingrese su primer número: "))
number_two=int(input("Ingrese su segundo número: "))
number_three=int(input("Ingrese su tercer número: "))

if number_one == 30 or number_two ==30 or number_three ==30:
    print("Correcto")
elif number_one+number_two+number_three==30:
    print("Correcto")
else:
    print("Incorrecto")
