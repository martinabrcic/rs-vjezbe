def filtriranje_parnih(lista, m):
    lista_parnih = []
    while m <= len(lista):
        if m%2 == 0:
            lista_parnih.append(m)
        m+=1
    return lista_parnih
print(filtriranje_parnih([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],1))
