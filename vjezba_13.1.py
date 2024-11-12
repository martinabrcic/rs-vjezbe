lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def prvi_i_zadnji(lista):

    nova_lista = []
    prvi = lista[0]

    duljina_liste = len(lista)
    
    zadnji = duljina_liste

    nova_lista.append(prvi)
    nova_lista.append(zadnji)

    novi_tuple = tuple(nova_lista)

    return novi_tuple

print(prvi_i_zadnji(lista)) # (1, 10)