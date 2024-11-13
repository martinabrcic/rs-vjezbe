def duplikati(lista):
    lista_cista = []
    for x in lista:
        if x not in lista_cista:
            lista_cista.append(x)
        else:
            print(f"Duplikat: {x}")
    return lista_cista

print(duplikati([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
