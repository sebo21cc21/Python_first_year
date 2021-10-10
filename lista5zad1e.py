"""
@author: Sebastian Bednarski
"""
import stos

def sprawdzenie_stosu_mieszane(napis):
    """Funkcja, ktora sprawdza poprawnosc otwierania i zamykania mieszanych nawiasow 
    
    Args:
        napis (string): ciag znakow, w którym badamy poprawne rozmieszczenie np. "()", ilosc nawiasow- pary oraz typ nawiasow 

    Returns:
        bool: wartość logiczna True, gdy nawiasy są prawidlowo dobrane
        w przecinwym wypadku: wartośc logiczna False
     """
    moj_stos = stos.utworz_stos()
    slownik = {')': '(', ']': '[', '}': '{'}

    for nawias in napis:
        if nawias in ("(", "{", "["):
            stos.na_stos(moj_stos, nawias)
        elif nawias in (")", "}", "]"):
            klamra = stos.ze_stosu(moj_stos)
            if klamra is None or slownik.get(nawias) != klamra:
                return False

    if moj_stos.wierzch is None: #jesli stos pusty, czyli wszystkie nawiasy maja pare zwraca bool: True
        return True 
    return False

def test_sprawdzenie_stosu_mieszane():
    """
    Funkcja testujaca funkcje sprawdzenie_stosu_mieszane(napis)
    """
    napis = "max{a*[b+(1/c)], e/[1+f]} "
    assert sprawdzenie_stosu_mieszane(napis) is True, "Zle sprawdzenie wystepownia nawiasow mieszanych"
    print(napis, "- prawidlowe nawiasy.")

    napis = "max{a*[b+(1/c], e/[1+f]} "
    assert sprawdzenie_stosu_mieszane(napis) is False, "Zle sprawdzenie wystepownia nawiasow mieszanych"
    print(napis, "- nieprawidlowe nawiasy.")

    napis = "max{a*[b+(1/c], e/[1+f])}"
    assert sprawdzenie_stosu_mieszane(napis) is False, "Zle sprawdzenie wystepownia nawiasow mieszanych"
    print(napis, "- nieprawidlowe nawiasy.")

test_sprawdzenie_stosu_mieszane()
