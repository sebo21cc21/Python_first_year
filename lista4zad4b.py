"""
@author: Sebastian Bednarski
"""
from lista4zad4 import *
import time
import random

lista_losowa_1 = random.sample(range(1, int(1e6)), int(1e1))
lista_losowa_2 = random.sample(range(1, int(1e6)), int(1e2))
lista_losowa_3 = random.sample(range(1, int(1e6)), int(1e3))
lista_losowa_4 = random.sample(range(1, int(1e6)), int(1e4))

def pomiar_czasu(lista):
    start = time.time()
    Sortowanie_szybkie(list(lista), 0, len(lista) - 1)
    czas = time.time() - start
    print('Sortowanie szybkie, czas:', czas)

    start = time.time()
    Sortowanie_babelkowe(list(lista))
    czas = time.time() - start
    print('Sortowanie babelkowe, czas:', czas)

    start = time.time()
    The_best_sort(list(lista), 0, len(lista) - 1)
    czas = time.time() - start
    print('The best sort, czas:', czas)


print('===10 ELEMENTOW===')
pomiar_czasu(lista_losowa_1)
print('===100 ELEMENTOW===')
pomiar_czasu(lista_losowa_2)
print('===1000 ELEMENTOW===')
pomiar_czasu(lista_losowa_3)
print('===10000 ELEMENTOW===')
pomiar_czasu(lista_losowa_4)