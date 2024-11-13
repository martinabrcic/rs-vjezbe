tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

def brojanje_rijeci(tekst):

    rjecnik = {}

    interpunkcija = ".,!?;:"
    for znak in interpunkcija:
        tekst = tekst.replace(znak,'')
    
    rijeci = tekst.split()

    for rijec in rijeci:
        if rijec in rjecnik:
            rjecnik[rijec] += 1
        else:
            rjecnik[rijec] = 1
    
    return rjecnik

print(brojanje_rijeci(tekst))

# {'Python': 2, 'je': 3, 'programski': 1, 'jezik': 1, 'koji': 1, 'jednostavan': 1, 'za': 1, 'učenje': 1, 'i': 1, 'korištenje.': 1, 'vrlo': 1, 'popularan.': 1}