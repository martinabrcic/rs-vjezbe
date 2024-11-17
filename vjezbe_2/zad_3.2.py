#Koristeći list comprehension, izgradite listu duljina svih nizova u listi rijeci, ali samo za nizove koji sadrže slovo a:

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]

duljine_sa_slovom_a = [len(rijec) for rijec in rijeci if "a" in rijec]

print(duljine_sa_slovom_a) # [6, 3, 6, 8, 9, 8, 6, 17]