"""
@author: Sebastian Bednarski
"""

def zliczanie_wystapien(tablica, x, pozycja, licznik):
    """ Funckja do liczenia wystapien elementow w tablicy- wykonana samodzielnie na zajeciach
    Args:
        tab (list): tablica podanych elementow #moga byc typu float argumenty
        x (float): sprawdzany element
        pozycja (int): pozycja kolejnych sprawdzanych elementow
        licznik (int): przechwouje liczbe powtorzen danego elementu i zwieksza sie

    Returns: 
        int: ilosc powtorzen elementu x w tablicy tab  #tu jest typu int, gdyż nie będzie powtarzalo sie coś 0.5 raza
    """
    if pozycja < len(tablica):
        if not tablica[pozycja] == x:
            return zliczanie_wystapien(tablica, x, pozycja + 1, licznik)
        else:
            return zliczanie_wystapien(tablica, x, pozycja + 1, licznik + 1)
    else: 
        return licznik

def zliczanie_wystapien_2(tab, x, pozycja):
    """ Funckja do liczenia wystapien elementow w tablicy- ciekawsza, kod z lekcji
    Args:
        tab (list): tablica podanych elementow #moga byc typu float argumenty
        x (float): sprawdzany element
        pozycja (int): pozycja kolejnych sprawdzanych elementow

    Returns: 
        int: ilosc powtorzen elementu x w tablicy tab  #tu jest typu int, gdyż nie będzie powtarzalo sie coś 0.5 raza
    """
    if pozycja == len(tab):
        return 0 #warunek konca, jesli dlugosc rowna sie pozycji zwraca 0 np. pusta tablica od razu zwroci 0
    return zliczanie_wystapien_2(tab, x, pozycja + 1) + (tab[pozycja] == x) #zmienna typu bool dodajemy 1 albo 0 i dostaniemy liczbe wystapien danego elementu

def test_zliczanie_wystapien():
    """Funkcja testujaca funkcje zliczanie wystapien"""
    test = zliczanie_wystapien([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 0, 0)
    assert test == 1, 'Funkcja nieprawidlowa'
    print('Element wystapil: ', test, ' razy')

    test = zliczanie_wystapien([-1, 0, 3, -1], -1, 0, 0) #z ujemnnymi
    assert test == 2, 'Funkcja nieprawidlowa'
    print('Element wystapil: ', test, ' razy')

    test = zliczanie_wystapien([-1.5, 0, 3.2, -1.5, -1.2, -1.5], -1.5, 0, 0) #typu float
    assert test == 3, 'Funkcja nieprawidlowa'
    print('Element wystapil: ', test, ' razy')

    test = zliczanie_wystapien([], 5, 0, 0) #sprawdzanie dla pustej tablicy
    assert test == 0, 'Funkcja nieprawidlowa'
    print('Tablica pusta, element wystapil: ', test, ' razy')
    
    test = zliczanie_wystapien([-5, -7, 0, 1000, 7, 2020,], 5, 0, 0) #sprawdzanie dla elementu spoza tablicy
    assert test == 0, 'Funkcja nieprawidlowa'
    print('Element x poza tablicą, zwraca ilosc powtorzen rowna: ', test, ' razy')


def test_zliczanie_wystapien_2():
    """Funkcja testujaca funkcje zliczanie wystapien"""
    test = zliczanie_wystapien_2([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 0)
    assert test == 1, 'Funkcja nieprawidlowa'
    print('Element wystapil: ', test, ' razy')

    test = zliczanie_wystapien_2([-1, 0, 3, -1], -1, 0)
    assert test == 2, 'Funkcja nieprawidlowa'
    print('Element wystapil: ', test, ' razy')

    test = zliczanie_wystapien_2([-1.5, 0, 3.2, -1.5, -1.2, -1.5], -1.5, 0)
    assert test == 3, 'Funkcja nieprawidlowa'
    print('Element wystapil: ', test, ' razy')

    test = zliczanie_wystapien_2([], 5, 0)
    assert test == 0, 'Funkcja nieprawidlowa'
    print('Tablica pusta, element wystapil: ', test, ' razy')

    test = zliczanie_wystapien_2([-5, -7, 0, 1000, 7, 2020,], 5, 0) 
    assert test == 0, 'Funkcja nieprawidlowa'
    print('Element x poza tablicą, zwraca ilosc powtorzen rowna: ', test, ' razy')

test_zliczanie_wystapien()
test_zliczanie_wystapien_2()