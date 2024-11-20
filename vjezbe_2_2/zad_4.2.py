#Definirajte klasu Kalkulator s atributima a i b. Dodajte metode zbroj, oduzimanje, mnozenje, dijeljenje, potenciranje i korijen koje će izvršavati odgovarajuće operacije nad atributima a i b.
import math

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b
    
    def mnozenje(self):
        return self.a * self.b
    
    def dijeljenje(self):
        if self.b != 0:
            return self.a / self.b
        else:
            print("S nulom se ne dijeli")
    
    def potenciranje(self):
        return self.a ** self.b
    
    def korijen(self):
        korijen_a = math.sqrt(self.a)
        korijen_b = math.sqrt(self.b)

        return korijen_a, korijen_b

izracun = Kalkulator(2, 0)

print(izracun.zbroj())
print(izracun.oduzimanje())
print(izracun.mnozenje())
print(izracun.dijeljenje())
print(izracun.potenciranje())
print(izracun.korijen())

