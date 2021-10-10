"""
@author: Sebastian Bednarski
zrodlo: algorytm z lekcji
"""

"""
Wykorzystany algorytm:

0. Mamy napis.
1. Niech n := dlugosc(napis)
2. Jesli n jest równe zero lub n nie jest liczba parzysta:
3. Zwracamy wartosc FAŁSZ i algorytm konczy sie.
4. W przeciwnym wypadku:
5. Niech i :=0
6. Dopóki i jest mniejsze niz n/2:
7. Jesli element tablicy na pozycji i jest rózny od 'a'
lub element tablicy na pozycji (n-i-1) jest rózny od 'b':
8. Zwracamy wartosc FAŁSZ i algorytm konczy sie.
9. W przeciwnym wypadku:
10. Zwiekszamy i o 1.
11. Wracamy do pkt 6.
12. Zwracamy wartosc PRAWDA i algorytm konczy sie.

kod przed funkcją:
napis = ['a', 'a', 'b', 'b']
n = len(napis)
if n == 0 or n%2 != 0:
    print('FAŁSZ')
else: 
    i = 0
    while i < n/2:
        if(napis[i] != 'a' or napis[n-i-1] != 'b' ):
            print('FAŁSZ')
        else:
            i+=1
    print('PRAWDA')
"""
def funkcja_czy_napis(napis):
    """ Funckja do posortowania elementow w tablicy
    Args:
        tab (list): tablica podanych elementow #moga byc typu float argumenty

    Returns: 
        list: tablica posortowanych elementów
    """
    n = len(napis) #dlugosc tablicy
    if n == 0 or n%2 != 0: #warunki niespełnienia
        return False #nie nalezy do jezyka
    else: #przeciwny wypadek
        i = 0
        while i < n/2: #2 razy mniejsza długosc od tablicy, gdyż sprawdzamy po połowie aa||bb
            if(napis[i] != 'a' or napis[n-i-1] != 'b' ): #warunki sprawdzania od początku części a oraz od końca częsci b
                return False #nie nalezy do jezyka
            else:
                i+=1 #inkrementacja
        return True #nalezy do jezyka
    
def test_funkcja_czy_napis():
    """ Funkcja testująca funkcje funkcja_czy_napis"""
    napis = ['a', 'a', 'b', 'b']
    napis2 = ""
    test = funkcja_czy_napis(napis)
    assert test == True, 'FAŁSZ'
    for i in range(len(napis)):
        napis2 += napis[i]
    print(napis2, '- nalezy do jezyka')

    napis = ['a', 'a', 'a', 'b', 'b', 'b']
    napis2 = ""
    test = funkcja_czy_napis(napis)
    assert test == True, 'FAŁSZ'
    for i in range(len(napis)):
        napis2 += napis[i]
    print(napis2, '- nalezy do jezyka')

    napis = []
    napis2 = ""
    test = funkcja_czy_napis(napis)
    assert test == False, 'FAŁSZ'
    for i in range(len(napis)):
        napis2 += napis[i]
    print(napis2, '- nie nalezy do jezyka')

    napis = ['a', 'c', 'b']
    napis2 = ""
    test = funkcja_czy_napis(napis)
    assert test == False, 'FAŁSZ'
    for i in range(len(napis)):
        napis2 += napis[i]
    print(napis2, '- nie nalezy do jezyka')

    napis = ['a', 'b', 'b']
    napis2 = ""
    test = funkcja_czy_napis(napis)
    assert test == False, 'FAŁSZ'
    for i in range(len(napis)):
        napis2 += napis[i]
    print(napis2, '- nie nalezy do jezyka')

test_funkcja_czy_napis()