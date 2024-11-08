lozinka = input("Unesite lozinku: ")

def provjera_lozinke(lozinka):

    has_letter = False
    has_digit = False

    for i in lozinka:
        if i.isalpha():
            has_letter = True
        if i.isdigit():
            has_digit = True
        

    if len(lozinka) < 8 and len(lozinka) > 15:
        print("Lozinka mora biti dulja od 8 i kraća od 15!")
    elif lozinka.lower() == "lozinka" or lozinka.lower() == "password":
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
    elif not has_letter or not has_digit:
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
    else:
        print("Lozinka je jaka! " + lozinka)

provjera_lozinke(lozinka)