"""
@author: Sebastian Bednarski
Zadania 1 oraz 3 są spełnione, wiec pokaze tylko 2 :)
"""
def wyszukiwanie_binarne_5(tab, start, mid, end, x):
    """ Funckja do wyszukiwania binarnego
    Args:
        tab (list): tablica podanych elementow POSORTOWANA!
        start (int): początek zakresu wyszukiwań
        mid (int): srodek zakresu
        end (int): koniec zakresu szukania
        x (float): szukana liczba

    Returns: 
        int: numer indeksu szukanego elementu w tablicy
        None: w przeciwnym wypadku
    """
    if start > end:
        return None
    else:
        if tab[mid] == x:
            return mid
        elif tab[mid] < x:          
            return wyszukiwanie_binarne_5(tab, mid + 1, ( mid + 1 + end ) // 2, end, x) #zamiast mid piszemy jego wartosc w wywolaniu rekurencyjnym
        elif tab[mid] > x:
            return wyszukiwanie_binarne_5(tab, start, (start + mid - 1) // 2, mid - 1, x)

def test_wyszukiwanie_binarne_5():
    """Funkcja testujaca wyszukiwanie binarne"""
    test = wyszukiwanie_binarne_5([1, 3, 5, 6, 7, 9, 11], 0, 3, 6, 3)
    assert test == 1, 'Nieprawidlowo wyszukany element- zla funkcja'
    print('Wyszukiwany element ma w tablicy indeks: ' + str(test))

    test = wyszukiwanie_binarne_5([-33, -11, 5, 9, 11], 0, 2, 4, -11)
    assert test == 1, 'Nieprawidlowo wyszukany element- zla funkcja'
    print('Wyszukiwany element ma w tablicy indeks: ' + str(test))

    test = wyszukiwanie_binarne_5([-1000, -222.22, -11.3, -6.2, 7.6, 19.1, 1142.10, 100000.00], 3, 5, 7, 1142.10)
    assert test == 6, 'Nieprawidlowo wyszukany element- zla funkcja'
    print('Wyszukiwany element ma w tablicy indeks: ' + str(test))

    test = wyszukiwanie_binarne_5([1000, 2, 4, 7, 1], 0, 2, 4, 1) #nieposortowana nie działa
    assert test == None, 'Nieprawidlowo wyszukany element- zla funkcja'
    print('Wyszukiwany element ma w tablicy indeks: ' + str(test))

    test = wyszukiwanie_binarne_5([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 4, 8, 10) #element spoza tablicy
    assert test == None, 'Nieprawidlowo wyszukany element- zla funkcja'
    print('Element nie znajduje sie w tablicy, zwraca: ' + str(test))
test_wyszukiwanie_binarne_5()
