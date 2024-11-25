
class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina

    def ispis(self):
        print(f"Atributi: naziv - {self.naziv}, cijena: {self.cijena}, kolicina: {self.kolicina}")

proizvodi = []
proizvod_1 = Proizvod("Čokolada", 1.99, 2)
proizvod_2 = Proizvod("Čips", 2.20, 3)
proizvodi.append(proizvod_1)
proizvodi.append(proizvod_2)

def dodaj_proizvod(naziv, cijena, kolicina):
    novi_proizvod = Proizvod(naziv, cijena, kolicina)
    proizvodi.append(novi_proizvod)
    print(f"Proizvod {naziv} dodan u listu!")



        