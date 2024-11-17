#vrati True ako je broj paran, inače vrati None

def paran_broj(x):
    if x % 2 == 0:
        return True
    else:
        return False

provjera_parnosti = lambda x: [True if x % 2 == 0 else False]
print(provjera_parnosti(6))