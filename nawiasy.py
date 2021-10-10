
'''
na postawie kodu zaprezontowanego na wykładzie oraz labolatorium

'''
import stos

def nawias_okr(napis):
    """Funkcja sprawdzająca poprawność otwarcia i zamknęcia nawiasów okrągłych
    
    Args:
        napis (string): ciąg łańcuchów, w którym badamy poprawność ilości i
        rozmieszczenia nawiasów okrągłych

    Returns:
        bool: wartość logiczna True gdy nawiasy są prawidłowo użyte i rozmieszczone
        w przecinwym wypadku: wartośc logiczna False
     """
    nowy_stos = stos.utworz_stos()

    for znak in napis:
        if znak == "(":
            stos.na_stos(nowy_stos, znak)
        elif znak == ")":
            if stos.ze_stosu(nowy_stos) is None:
                return False

    if nowy_stos.wierzch is None:
        return True 
    return False


def test_nawias_okr(): #funkcja testująca do funkcji nawias_okr(napis)
    napis = "max(a, max(b,c))"
    assert nawias_okr(napis) is True, "Źle sprawdzone wystepownie nawiasów okrągłych"
    print("W tekście", napis, "nawiasy wystepują prawidłowo.")

    napis = "max(a, max(b,c)"
    assert nawias_okr(napis) is False, "Źle sprawdzone wystepownie nawiasów okrągłych"
    print("W tekście", napis, "nawiasy nie wystepują prawidłowo.")

    napis = "nucegydwuqjp9{jdtev}]0))"
    assert nawias_okr(napis) is False, "Źle sprawdzone wystepownie nawiasów okrągłych"
    print("W tekście", napis, "nawiasy nie wystepują prawidłowo.")
test_nawias_okr()