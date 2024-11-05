
g = int(input("Molim vas unesite godinu: "))


if(g % 4 == 0 and not g % 100 == 0) or (g % 400 == 0):
    print("Godina " + str(g) + " je prijestupna!")
else:
    print("Godina " + str(g) + " nije prijestupna!")


