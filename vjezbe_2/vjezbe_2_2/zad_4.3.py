#Definirajte klasu Student s atributima ime, prezime, godine i ocjene.
#Iterirajte kroz sljedeću listu studenata i za svakog studenta stvorite objekt klase Student i dodajte ga u novu listu studenti_objekti:

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime 
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        if self.ocjene:
            return sum(self.ocjene) / len(self.ocjene)
        else:
            return 0

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = []

for student in studenti:
    novi_student = Student(student["ime"], student["prezime"], student["godine"], student["ocjene"])
    studenti_objekti.append(novi_student)

for student in studenti_objekti:
    print(f"Student: {student.ime} {student.prezime}, Godine: {student.godine}, ocjene: {student.ocjene}, prosjek: {student.prosjek()}")

najbolji_student = max(studenti_objekti, key=lambda student: student.prosjek())
print(f"Najbolji student je: {najbolji_student.ime} {najbolji_student.prezime}, Prosjek: {najbolji_student.prosjek()}")