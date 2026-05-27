#Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def read_songs(path_one, path_two):
    with open(path_one, 'r', encoding='utf-8') as file:
        songs = file.readlines()

    songs = [song.strip() for song in songs]

    songs.sort()

    with open(path_two, 'w', encoding='utf-8') as file:
        for song in songs:
            file.write(song + '\n')

    print(f'songs:{songs}')
    
read_songs('songs.txt', 'sort_songs.txt')