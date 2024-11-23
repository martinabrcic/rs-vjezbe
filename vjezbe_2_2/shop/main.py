from proizvodi import dodaj_proizvod, Proizvod, proizvodi

proizvodi_dict = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]

for i in proizvodi_dict:
    dodaj_proizvod(i["naziv"], i["cijena"], i["kolicina"])

for proizvod in proizvodi:
    proizvod.ispis()