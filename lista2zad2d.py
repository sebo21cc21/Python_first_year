"""
@author: Sebastian Bednarski
"""

def pokaz_ciag(a0, r, N):
    """ Funkcja pokazuje ciag arytmetyczny

    Args:
        a0 (float): wartosc poczatkowa tablicy
        r (float): roznica miedzy elementami #np. r=a[1]-a[0]
        N (int): ilosc elementow w tablicy #wartosci calkowite n > 0

    Returns:
        list: ciag arytmetyczny liczb, jesli podano poprawne dane #argumenty moga byc typu float
        None: w przeciwnym wypadku
    """
    if N > 0:
        a = [a0]
        i = 0
        for i in range(N-1):
            a.append(r + a[i])
        return a
    else:
        return None

def test_pokaz_ciag():
    """ Funkcja testujaca funkcje pokaz_ciag(a0, r, N) """
    a = pokaz_ciag(3, 5, 4) #sprawdzenie z zadania 1d
    assert a == [3, 8, 13, 18], 'Nieprawidlowy zapis funkcji- bledna wartosc'
    print('Ciag arytmetyczny jest postaci: ' + str(a))

    """ Funkcja testujaca funkcje pokaz_ciag(a0, r, N) """
    a = pokaz_ciag(3.6, 5.3, 4) #sprawdzenie dla typu float
    assert a == [3.6, 8.9, 14.2, 19.5], 'Nieprawidlowy zapis funkcji- bledna wartosc'
    print('Ciag arytmetyczny jest postaci: ' + str(a))

test_pokaz_ciag()