#Definirajte varijablu min_duljina koja će pohranjivati int. Koristeći odgovarajuću funkciju višeg reda i lambda izraz, pohranite u varijablu duge_rijeci sve riječi iz liste rijeci koje su dulje od min_duljina:


rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]

min_duljina = int(input("Unesite minimalnu duljinu riječi: "))

duge_rijeci = list(filter(lambda rijec : len(rijec) > min_duljina, rijeci))

print(duge_rijeci) # ['zvijezda', 'prijatelj', 'čokolada', 'otorinolaringolog']