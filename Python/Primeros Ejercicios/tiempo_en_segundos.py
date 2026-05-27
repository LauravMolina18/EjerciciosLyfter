seconds=int(input("Ingrese un timepo en segundos: "))
if seconds < 600:
    seconds_left=600 - seconds
    print(f"Los segundos que faltan para llegar a 10 minutos son: {seconds_left}")
elif seconds>600:
    print("Mayor")
else:
    print("Igual")
