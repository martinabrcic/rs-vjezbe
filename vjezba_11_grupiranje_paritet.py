lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def grupiraj_po_paritetu(lista):

    rjecnik = {}
    lista_parni = []
    lista_neparni = []
    for i in lista:
        if i % 2 == 0:
            lista_parni.append(i)
        else:
            lista_neparni.append(i)
    
    rjecnik.update({'parni': lista_parni, 'neparni': lista_neparni})
    return rjecnik


print(grupiraj_po_paritetu(lista))

# {'parni': [2, 4, 6, 8, 10], 'neparni': [1, 3, 5, 7, 9]}