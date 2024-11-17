# Koristeći odgovarajuću funkciju višeg reda i lambda izraz (bez comprehensiona), pohranite u varijablu transform rezultat kvadriranja svih brojeva u listi gdje rezultat mora biti rječnik gdje su ključevi originalni brojevi, a vrijednosti kvadrati tih brojeva:

brojevi = [10, 5, 12, 15, 20]

def trans_fun(lista):

    rjecnik = {}

    for element in lista:
        rjecnik[element] = element ** 2
    return rjecnik

print(trans_fun(brojevi))

transform = dict(map(lambda el: (el, el ** 2), brojevi))

print(transform) # {10: 100, 5: 25, 12: 144, 15: 225, 20: 400}