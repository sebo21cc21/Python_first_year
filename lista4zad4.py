"""
@author: Sebastian Bednarski
Moduł z funkcjami do zadania 4
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

def podzial(tab, poczatek, koniec):
    """ Funkcja podzialu dla sortowania szybkiego.
    Args:
    tablica (list): lista elementow do uporzadkowania
    poczatek (int): poczatek zakresu
    koniec (int): koniec zakresu 
    Returns:
    int: indeks elementu osiowego
    """
    wartosc_podzialu = tab[koniec] #ustawiamy na ostatni element
    i = poczatek
    for j in range(poczatek, koniec):
        if tab[j] < wartosc_podzialu:
            tab[i], tab[j] = tab[j], tab[i] #swap
            i += 1 #zwiekszamy indeks poczatkowy
    tab[i], tab[koniec] = tab[koniec], tab[i] #swap
    return i

def Sortowanie_szybkie(tab, poczatek, koniec):
    """ Funkcja sortowania szybkiego danej tablicy ukazana na wykladzie
    Args:
    tablica (list): lista elementow do uporzadkowania
    poczatek (int): poczatek zakresu 
    koniec (int): koniec zakresu
    Returns:
    list: uporządkowana lista elementów
    """
    if poczatek < koniec:
        srodek = podzial(tab, poczatek, koniec)
        Sortowanie_szybkie(tab, poczatek, srodek - 1) #rekurencja i podstawienie
        Sortowanie_szybkie(tab, srodek + 1, koniec)
    return tab

def The_best_sort(tab, poczatek, koniec):
    """ Funkcja sortowania szybkiego polaczana z sortowaniem babelkowy.
    Args:
    tablica (list): lista elementow do uporzadkowania
    poczatek (int): poczatek zakresu 
    koniec (int): koniec zakresu
    Returns:
    list: uporządkowana lista elementów
    """
    if poczatek < koniec:
        if len(tab) < 7:
            Sortowanie_babelkowe(tab)
        else:
            Sortowanie_szybkie(tab, poczatek, koniec)
    return tab

def test_The_best_sort():
    """Funkcja testujaca funkcje The_best_sort"""
    posortowane = The_best_sort([5, 14, 2, 1, -5, 2, 199, 200, 131], 0, 8) #sprawdzenie 9 wymiarowej z minusowymi
    assert posortowane == [-5, 1, 2, 2, 5, 14, 131, 199, 200], 'Blednie posortowane'
    print('Posortowana tablica ma wartosci: ', posortowane)

    posortowane = The_best_sort([-5, 155.22, 22, -999, 14, 12312312, -1441.13, 414114, 519, 11, 313, -142, -142], 0, 12)
    assert posortowane == [-1441.13, -999, -142, -142, -5, 11, 14, 22, 155.22, 313, 519, 414114, 12312312], 'Blednie posortowane'
    print('Posortowana tablica ma wartosci: ', posortowane)

    posortowane = The_best_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 9) #wszystko do zmiany
    assert posortowane == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'Blednie posortowane'
    print('Posortowana tablica ma wartosci: ', posortowane)

    posortowane = The_best_sort([1, 2, 1], 0, 2) #sprawdzenie tych samych wartosci
    assert posortowane == [1, 1, 2], 'Blednie posortowane'
    print('Posortowana tablica ma wartosci: ', posortowane)

    posortowane = The_best_sort([1, 1.1, 1.2, 1], 0, 3) #sprawdzenie tych samych wartosci
    assert posortowane == [1, 1, 1.1, 1.2], 'Blednie posortowane'
    print('Posortowana tablica ma wartosci: ', posortowane)

    posortowane = The_best_sort([2, 1], 0, 1) #sprawdzenie tych samych wartosci
    assert posortowane == [1, 2], 'Blednie posortowane'
    print('Posortowana tablica ma wartosci: ', posortowane)

    posortowane = The_best_sort([12], 0, 0)
    assert posortowane == [12], 'Blednie posortowane'
    print('Posortowana tablica ma wartosci: ', posortowane)

    posortowane = The_best_sort([], 0, -1) #sprawdzenie pustej
    assert posortowane == [], 'Blednie posortowane'
    print('Posortowana tablica ma wartosci: ', posortowane)

test_The_best_sort()
