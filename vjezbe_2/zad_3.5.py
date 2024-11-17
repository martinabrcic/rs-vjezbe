#Koristeći list comprehension, izgradite listu rječnika gdje su ključevi prezimena studenata, a vrijednosti su zbrojeni bodovi, iz liste studenti:

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
    {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
    {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
    {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
    {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]

zbrojeni_bodovi = [{student["prezime"]: sum(student["bodovi"])} for student in studenti]

print(zbrojeni_bodovi) # [{'Ivić': 152}, {'Marković': 127}, {'Anić': 55}, {'Petrić': 362}, {'Ivić': 236}, {'Matić': 266}]

zbroj_bodova = []

for student in studenti:
    prezime = student["prezime"]
    bodovi = student["bodovi"]
    zbroj_bodova.append({prezime: sum(bodovi)})

print(zbroj_bodova)