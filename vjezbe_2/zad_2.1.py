#koristeći funkciju map, kvadrirajte duljine svih nizova u listi

niz = ["jabuka", "kruška", "banana", "naranča"]

kvadrirane_duljine = list(map(lambda element: len(element) ** 2, niz))

print(kvadrirane_duljine)