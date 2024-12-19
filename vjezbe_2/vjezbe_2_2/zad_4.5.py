
class Radnik:

    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print (f"Radim na poziciji {self.pozicija}")


class Manager(Radnik):

    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def give_raise(self, radnik, povecanje):
        
        nova = radnik.placa + povecanje
        print(f"Nova placa radnika je {nova}")
    

radnik = Radnik("Niko", "IT support", 12345)
manager = Manager("Ivo", "menadžer", 22222, "IT")

radnik.work()
manager.give_raise(radnik, 122)
    
