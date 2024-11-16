#koristeći funkciju filter, filtrirajte samo brojeve veće od 5

brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]

veci_od_5 = list(filter(lambda broj : broj > 5, brojevi))

print(veci_od_5)