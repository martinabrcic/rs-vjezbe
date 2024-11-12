skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}

def presjek(skup_1, skup_2):

    lista = []

    for i in skup_1:
        if i in skup_2 and i not in lista: 
            lista.append(i)  
    return lista

print(presjek(skup_1, skup_2)) # {4, 5}