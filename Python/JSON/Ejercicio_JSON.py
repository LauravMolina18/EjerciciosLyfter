#Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON

import json

def read_pokemon_file(filename):
    with open(filename, "r") as file:
        pokemon_list = json.load(file)
    return pokemon_list


def get_new_pokemon():
    name = input("Nombre del Pokémon: ")
    type_ = input("Tipo: ")
    level = int(input("Nivel: "))
    weight = float(input("Peso kg: "))
    is_shiny = input("¿Es shiny? (si/no): ").lower() == "si"

    held_item = input("Objeto equipado (deja vacío si no tiene): ")
    if held_item == "":
        held_item = None

    skills = []
    print("Ingresa 4 habilidades:")
    for i in range(4):
        skill = input(f"Habilidad {i+1}: ")
        skills.append(skill)

    print("Ingresa los stats:")
    hp = int(input("HP: "))
    attack = int(input("Ataque: "))
    defense = int(input("Defensa: "))
    sp_attack = int(input("Ataque especial: "))
    sp_defense = int(input("Defensa especial: "))
    speed = int(input("Velocidad: "))

    new_pokemon = {
        "name": name,
        "type": type_,
        "level": level,
        "weight_kg": weight,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": {
            "hp": hp,
            "attack": attack,
            "defense": defense,
            "sp_attack": sp_attack,
            "sp_defense": sp_defense,
            "speed": speed
        }
    }

    return new_pokemon


def save_pokemon_file(filename, pokemon_list):
    with open(filename, "w") as file:
        json.dump(pokemon_list, file, indent=4)


def main():
    filename = "pokemon.json"

    pokemon_list = read_pokemon_file(filename)
    new_pokemon = get_new_pokemon()
    pokemon_list.append(new_pokemon)
    save_pokemon_file(filename, pokemon_list)

    print("Pokémon agregado")


main()