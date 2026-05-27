#cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.

import csv

games = []

game_number = int(input('Cuántos videojuegos quieres ingresar?: '))

for i in range(game_number):
    print(f'\nVideo Juego {i+1}: ')

    name = input("Nombre: ")
    genre = input("Género: ")
    developer = input("Desarrollador: ")
    esrb = input("Clasificación ESRB:")

    game = {
        "Name": name,
        "Genre": genre,
        "Developer": developer,
        "ESRB": esrb,
    }

    games.append(game)

with open("videojuegos.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Name", "Genre", "Developer", "ESRB"]
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter="\t")
    writer.writeheader()
    writer.writerows(games)

print('\nLos datos se gurdaron en el archivo videojuegos.csv')