lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

def maks_i_min(lista):

    nova_lista = []

    lista.sort()

    print(lista)

    najmanji = lista[0]
    najveci = lista[-1]

    nova_lista.append(najmanji)
    nova_lista.append(najveci)

    novi_tuple = tuple(nova_lista)

    return novi_tuple

print(maks_i_min(lista)) # (250, 5)