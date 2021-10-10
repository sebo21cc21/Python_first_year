"""maksimum = 0
pozycja = 0
tab = [1, 4, 5, 2]
while pozycja < len(tab):
    if tab[pozycja] > maksimum:
        maksimum = tab[pozycja]
    pozycja += 1
print(maksimum)
"""
def maksimum(tab):
    maksimum = 0
    pozycja = 0
    while pozycja < len(tab):
        if tab[pozycja] > maksimum:
            maksimum = tab[pozycja]
        pozycja += 1
    return maksimum
tab = [1, 4, 5, 2]
liczba = maksimum(tab)
print(liczba)