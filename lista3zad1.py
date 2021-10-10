"""
@author: Sebastian Bednarski
zrodlo: Wikipedia- Sortowanie babelkowe
"""
def Sortowanie_babelkowe(tab):    #definiuje tablice, wchodzi wartość tab
    """ Funckja do posortowania elementow w tablicy
    Args:
        tab (list): tablica podanych elementow #moga byc typu float argumenty

    Returns: 
        list: tablica posortowanych elementów
    """
    for j in range(len(tab) - 1):    #pierwsza pętla rozmiar zmienny o 1, j zaczyna się od 0
        for j in range(len(tab) - 1 - j):   #pętla po pętli- zmiana dynamiczna o j, zmiana statyczna o 1 (bo tablica ma pierwszy element jako 0)
            if tab[j] > tab[j + 1]:   #warunek zmiany
                tab[j], tab[j + 1] = tab[j + 1], tab[j] #zamiana
    return tab

def test_Sortowanie_babelkowe():
    """Funkcja testujaca funkcje Sortowanie babelkowe"""
    posortowane = Sortowanie_babelkowe([5, 14, 2, 1, -5]) #sprawdzenie 5 wymiarowej z minusowymi
    assert posortowane == [-5, 1, 2, 5, 14], 'Blednie posortowane'
    print('Posortowana tablica ma wartosci: ', posortowane)

    posortowane = Sortowanie_babelkowe([-5, 155.22, 22, -999, 14])
    assert posortowane == [-999, -5, 14, 22, 155.22], 'Blednie posortowane'
    print('Posortowana tablica ma wartosci: ', posortowane)

    posortowane = Sortowanie_babelkowe([12, -100, 14])
    assert posortowane == [-100, 12, 14], 'Blednie posortowane'
    print('Posortowana tablica ma wartosci: ', posortowane)

    posortowane = Sortowanie_babelkowe([1, 2, 1]) #sprawdzenie tych samych wartosci
    assert posortowane == [1, 1, 2], 'Blednie posortowane'
    print('Posortowana tablica ma wartosci: ', posortowane)

    posortowane = Sortowanie_babelkowe([1, 1.1, 1.2, 1]) #sprawdzenie tych samych wartosci
    assert posortowane == [1, 1, 1.1, 1.2], 'Blednie posortowane'
    print('Posortowana tablica ma wartosci: ', posortowane)

    posortowane = Sortowanie_babelkowe([2, 1]) #sprawdzenie tych samych wartosci
    assert posortowane == [1, 2], 'Blednie posortowane'
    print('Posortowana tablica ma wartosci: ', posortowane)

    posortowane = Sortowanie_babelkowe([12])
    assert posortowane == [12], 'Blednie posortowane'
    print('Posortowana tablica ma wartosci: ', posortowane)

    posortowane = Sortowanie_babelkowe([])
    assert posortowane == [], 'Blednie posortowane'
    print('Posortowana tablica ma wartosci: ', posortowane)



test_Sortowanie_babelkowe()


