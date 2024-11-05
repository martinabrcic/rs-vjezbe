
target = 44

brojac = 0
broj = 0

while broj != target:
    
    broj = int(input("Unesite broj od 1 do 100: "))
    brojac+=1
    if(broj < target and broj <= 100 and broj > 0):
        print("Uneseni broj je manji od traženoga!")
        
    elif(broj > target and broj <= 100 and broj > 0):
        print("Uneseni broj je veći od traženoga!")
        
    elif(broj == target):
        print("Bravo, pogodio si u " + str(brojac) + " pokusaja!")
    else:
        print("Krivi unos! Unesite broj od 1 do 100!")
        