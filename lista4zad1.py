"""
@author: Sebastian Bednarski
zrodlo: http://math.uni.wroc.pl/~jagiella/files/p1python/rekurencja.pdf
"""

def nwd(a, b):
    """ Funckja do wyszukania najwiekszego wspolnego dzielnika
    Args:
        a (int): pierwsza sprawdzana liczba
        b (int): druga sprawdzana liczba

    Returns: 
        int: najwiekszy wspolny dzielnik
    """
    if b == 0:
        return abs(a)  #wartosc dodatnia- bezwzgledna
    return nwd(b, a%b) #rekurencja- pod a podstawia b, pod b podstawia reszta z dzielenia a na b

def test_nwd():
    """Funkcja testujaca funkcje nwd"""
    test = nwd(-8, 122)
    assert test == 2, 'bledna funkcja'
    print('Najwiekszy wspolny dzielnik podanych liczb wynosi: ' + str(test))

    test = nwd(-5, -2)
    assert test == 1, 'bledna funkcja'
    print('Najwiekszy wspolny dzielnik podanych liczb wynosi: ' + str(test))

    test = nwd(6, 12)
    assert test == 6, 'bledna funkcja'
    print('Najwiekszy wspolny dzielnik podanych liczb wynosi: ' + str(test))

    test = nwd(16098, 7)
    assert test == 1, 'bledna funkcja'
    print('Najwiekszy wspolny dzielnik podanych liczb wynosi: ' + str(test))

    test = nwd(146, -7)
    assert test == 1, 'bledna funkcja'
    print('Najwiekszy wspolny dzielnik podanych liczb wynosi: ' + str(test))


test_nwd()