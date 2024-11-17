#pomnoži vrijednost s 5 pa potenciraj na x

def pomnozi_i_potenciraj(x, y):
    return (y ** 5) ** x
print(pomnozi_i_potenciraj(1, 3))

pomnozi_pa_potenciraj = lambda x, y: (y ** 5) ** x
print(pomnozi_pa_potenciraj(1, 2))