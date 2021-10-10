"""
@author: Sebastian Bednarski
wyjasnienione na zajeciach
"""
import stos

def sprawdzenie_stosu(napis):
    """Funkcja, ktora sprawdza poprawnosc otwierania i zamykania okraglych nawiasow 
    
    Args:
        napis (string): ciag znakow, w którym badamy poprawne rozmieszczenie np. "()" i ilosc nawiasow- pary

    Returns:
        bool: wartość logiczna True, gdy nawiasy są prawidłowe
        w przecinwym wypadku: wartośc logiczna False
     """
    moj_stos = stos.utworz_stos()

    for nawias in napis:
        if nawias == "(":
            stos.na_stos(moj_stos, nawias)
        elif nawias == ")":
            if stos.ze_stosu(moj_stos) is None:
                return False

    if moj_stos.wierzch is None: #jesli stos pusty, czyli wszystkie nawiasy maja pare zwraca bool: True
        return True 
    return False

def test_sprawdzenie_stosu():
    """
    Funkcja testujaca funkcje sprawdzenie_stosu(napis)
    """
    napis = "max(a, max(b,c))"
    assert sprawdzenie_stosu(napis) is True, "Zle sprawdzenie wystepownia nawiasow okraglych"
    print(napis, "- prawidlowe nawiasy.")

    napis = "max(a, max(b,c)"
    assert sprawdzenie_stosu(napis) is False, "Zle sprawdzenie wystepownia nawiasow okraglych"
    print(napis, "- nieprawidlowe nawiasy.")

    napis = "(byledopiatku))"
    assert sprawdzenie_stosu(napis) is False, "Zle sprawdzenie wystepownia nawiasow okraglych"
    print(napis, "- nieprawidlowe nawiasy.")

test_sprawdzenie_stosu()
