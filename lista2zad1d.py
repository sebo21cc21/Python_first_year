"""
@author: Sebastian Bednarski
"""
a0 = 3 #wyraz poczatkowy
r = 5 #roznica
N = 4 #liczba elementow do obliczenia
i = 0
a = [a0]
if N > 0:
    for i in range(N-1):
        a.append(r + a[i])
    print('Ciag przedstawia sie nastepujaco: ' + str(a))
else:
    'Liczba elementow mniejsza od 0, podaj ja jako liczba dodatnia - typu int'