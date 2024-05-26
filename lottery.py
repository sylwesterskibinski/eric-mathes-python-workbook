from random import choice,random

lista = [3,3]


results = []

for _ in range(3):
    result = choice(lista)
    results.append(result)

if results == lista:
    print('Gratulacje trafione za pierwszym razem')
else:
    attempts = 1
    while results != lista:
        results = []
        for _ in range(3):
            result = choice(lista)
            results.append(result)
        attempts += 1
    print(f'Gratulacje, udało się po {attempts} próbach!')