"""
@author: Sebastian Bednarski
zrodlo: zajecia
"""
"""
Iteracja:
def wyszukiwanie_binarne_iteracja(tab, start, end, x):
    for i in tab:
        if start > end:
            return None
        else:
            mid = ((start + end) // 2)
            if tab[mid] == x:
                return mid
            elif tab[mid] < x:
                start = mid + 1
            elif tab[mid] > x:
                end = mid - 1
"""
def wyszukiwanie_binarne(tab, start, end, x):
    """ Funckja do wyszukiwania binarnego
    Args:
        tab (list): tablica podanych elementow POSORTOWANA!
        start (int): początek zakresu wyszukiwań
        end (int): koniec zakresu szukania
        x (float): szukana liczba

    Returns: 
        int: numer indeksu szukanego elementu w tablicy
        None: w przeciwnym wypadku
    """
    if start > end:
        return None
    else:
        mid = ((start + end) // 2) #dzielenie calkowite
        if tab[mid] == x:
            return mid
        elif tab[mid] < x:          
            return wyszukiwanie_binarne(tab, mid + 1, end, x) #rekurencja- za start = mid + 1
        elif tab[mid] > x:
            return wyszukiwanie_binarne(tab, start, mid - 1, x) #rekurencja- za end = mid - 1

def test_wyszukiwanie_binarne():
    """Funkcja testujaca wyszukiwanie binarne"""
    test = wyszukiwanie_binarne([1, 3, 5, 6, 7, 9, 11], 0, 6, 3)
    assert test == 1, 'Nieprawidlowo wyszukany element- zla funkcja'
    print('Wyszukiwany element ma w tablicy indeks: ' + str(test))

    test = wyszukiwanie_binarne([-33, -11, 5, 9, 11], 0, 4, -11) #dodajmy liczby ujemne
    assert test == 1, 'Nieprawidlowo wyszukany element- zla funkcja'
    print('Wyszukiwany element ma w tablicy indeks: ' + str(test))

    test = wyszukiwanie_binarne([-1000, -222.22, -11.3, -6.2, 7.6, 19.1, 1142.10, 100000.00], 3, 7, 1142.10) #szukanie od zakresu
    assert test == 6, 'Nieprawidlowo wyszukany element- zla funkcja'
    print('Wyszukiwany element ma w tablicy indeks: ' + str(test))

    test = wyszukiwanie_binarne([1000, 2, 4, 7, 1], 0, 4, 1) #nieposortowana nie działa
    assert test == None, 'Nieprawidlowo wyszukany element- zla funkcja'
    print('Nieposortowana tablica, zwrot: ' + str(test))

    test = wyszukiwanie_binarne([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8, 10) #element spoza tablicy
    assert test == None, 'Nieprawidlowo wyszukany element- zla funkcja'
    print('Element nie znajduje sie w tablicy, zwraca: ' + str(test))
test_wyszukiwanie_binarne()
