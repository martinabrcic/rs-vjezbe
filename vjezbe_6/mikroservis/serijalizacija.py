import json

in_memory_filmovi = []

try:
    with open('mikroservis/film.json', 'r') as file:
        in_memory_filmovi = json.load(file)
    
    if in_memory_filmovi:
        print("Filmovi su uspešno učitani i pohranjeni u memoriju.")
    else:
        print("Nema filmova u JSON fajlu.")

    print("\nPohranjeni filmovi u memoriji:")
    for film in in_memory_filmovi:
        print("\nFilm:")
        for atribut, vrednost in film.items():
            print(f"  {atribut}: {vrednost}")
        
except FileNotFoundError:
    print("Greška: File nije pronađen. Proveri putanju.")
except json.JSONDecodeError as e:
    print("Greška u JSON formatu: ", e)
except Exception as e:
    print("Nepoznata greška: ", e)
