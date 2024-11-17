# Definirajte klasu Automobil s atributima marka, model, godina_proizvodnje i kilometraža. Dodajte metodu ispis koja će ispisivati sve atribute automobila.

# Stvorite objekt klase Automobil s proizvoljnim vrijednostima atributa i pozovite metodu ispis.
# Dodajte novu metodu starost koja će ispisivati koliko je automobil star u godinama, trenutnu godine dohvatite pomoću datetime modula.
import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print(self.marka)
        print(self.model)
        print(self.godina_proizvodnje)
        print(self.kilometraza)

    def starost(self):
        trenutna_godina = datetime.date.today().year
        godine_starosti = trenutna_godina - self.godina_proizvodnje
        return f"Godine starosti su: {godine_starosti}"

auto = Automobil("Kia", "Ceed", 2017, 10000)
auto.ispis()
print(auto.starost())