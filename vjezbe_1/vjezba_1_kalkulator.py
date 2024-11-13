
a = float(input("Unesite prvi broj: "))
b = float(input("Unesite prvi broj: "))
o = input("Unesite operator +, -, * ili /: ")


if o == "+":
    print("Rezultat operacije " + str(a) + "+" + str(b) + " je " + str(a+b))
elif o == "-":
    print("Rezultat operacije " + str(a) + "-" + str(b) + " je " + str(a-b))
elif o == "*":
    print("Rezultat operacije " + str(a) + "*" + str(b) + " je " + str(a*b))
elif o == "/":
    if b == 0:
        print("Dijeljenje s 0 nije dozvoljeno!")
    else:
        print("Rezultat operacije " + str(a) + "/" + str(b) + " je " + str(a/b))
else:
    print("Nepodržani operator!")