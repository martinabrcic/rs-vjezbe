
rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

def obrni_rjecnik(rjecnik):
    
    novi_rjecnik = {}

    for key, value in rjecnik.items():

        novi_rjecnik[value] = key

    return novi_rjecnik

print(obrni_rjecnik(rjecnik))

# {'Ivan': 'ime', 'Ivić': 'prezime', 25: 'dob'}