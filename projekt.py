import turtle
import random
import time

window = turtle.Screen()


BOK = 600
X = -300
Y = 300
window.setup(BOK, BOK)
window.title('Kółko i krzyżyk')
window.bgpic("gwi.png")
window.bgcolor('black')
xo = turtle.Turtle()
xo.color('white')
xo.speed(0)
xo.pensize(7)
xo.hideturtle()
f = turtle.Turtle()
f.speed(0)
f.hideturtle()
kolej = 'X'
los = ['円', '蝶', '鼠', '花', '燭', '猫', '鬼', '亀', '蟒', '鳩', '草', '芹', '死']
xlos = random.choice(los)
los.remove(xlos)
olos = random.choice(los)
slownik = {'円': 'kółko', '蝶': 'motyl', '鼠': 'mysz', '花': 'kwiatek',
           '燭': 'świeca', '猫': 'kot', '鬼': 'zjawa', '亀': 'żółw',
           '蟒': 'wąż', '鳩': 'gołąb', '草': 'ziółko', '芹': 'pietruszka',
           '死': 'kostucha'}
Ooo = slownik[olos]
Xxx = slownik[xlos]

def block():
    window.onkey(None, 'Return')
    window.onkey(None, 'Left')
    window.onkey(None, 'Right')
def start(): #okno startowe
    block()
    global ugh
    ugh = True
    xo.clear()
    f.clear()
    xo.penup()
    xo.goto(-50, 110)
    xo.write("井字棋", font=("GB18030 Bitmap", 30))
    xo.penup()
    xo.goto(-100, 0)
    xo.write("Start", font=("Old School Adventures", 45))
    time.sleep(1.01)
    xo.penup()
    xo.goto(-230, -100)
    xo.write("- Wcisnij enter aby rozpoczac -", font=("Old School Adventures", 20))
    window.onkey(wybor, 'Return')
    turtle.onkey(turtle.bye, "Escape")
    print(ugh, 'start')

def wybor(): #wybor trybu gry
    block()
    xo.clear()
    xo.goto(-130, 120)
    xo.write("Tryb", font=("Old School Adventures", 70))
    xo.goto(120, -100)
    xo.write('漢字', font=("GB18030 Bitmap", 40))
    xo.goto(120, -130)
    xo.write('>>', font=("Old School Adventures", 20))
    xo.goto(-200, -130)
    xo.write('<<', font=("Old School Adventures", 20))
    xo.goto(-200, -75)
    xo.write('X vs. O', font=("Old School Adventures", 30))
    window.onkey(bitwa, 'Right')
    window.onkey(gra, 'Left')



def bitwa(): #pokazanie postaci
    global ugh
    ugh = False
    block()
    xo.clear()
    xo.goto(-100, 120)
    xo.write("Bitwa!", font=("Old School Adventures", 45))

    xo.goto(-200, -100)
    xo.write(olos, font=("GB18030 Bitmap", 90))

    xo.goto(120, -100)
    xo.write(xlos, font=("GB18030 Bitmap", 90))

    xo.goto(-200, -120)
    xo.write(Ooo, font=("GB18030 Bitmap", 40))

    xo.goto(120, -120)
    xo.write(Xxx, font=("GB18030 Bitmap", 40))

    window.onkey(gra, 'Return')
    print(ugh, 'bitwa2')

def gra():
    global ugh
    f.clear()
    xo.clear()
    block()
    tablica = [[None, None, None],
               [None, None, None],
               [None, None, None]]
    kolej = 'X'

    # linie

    ODSTĘP = int(BOK / 3)
    for a in [1, 2]:
        xo.penup()
        xo.goto(X + a * ODSTĘP, Y)
        xo.pendown()
        xo.goto(X + a * ODSTĘP, -Y)
        xo.penup()
        xo.goto(X, Y - a * ODSTĘP)
        xo.pendown()
        xo.goto(-X, Y - a * ODSTĘP)

    def punkty(p, q):  # punkty środkowe kwadratów, z których będą rysowane linie, jeśli będą 3 w rzędzie

        g = turtle.Turtle()
        g.pensize(10)
        g.pencolor("red")
        g.penup()
        g.goto(p)
        g.pendown()
        g.goto(q)
        g.hideturtle()
        time.sleep(1)
        g.reset()

    def sprawdz():

        # po skosie
        if tablica[0][0] == tablica[1][1] == tablica[2][2] and tablica[1][1] is not None:
            punkty((-200, 200), (200, -200))
            return tablica[2][2]

        if tablica[0][2] == tablica[1][1] == tablica[2][0] and tablica[1][1] is not None:
            punkty((-200, -200), (200, 200))
            return tablica[2][0]

        # w wierszu

        suma = 0
        for x in tablica:  # tutaj sumuję, ile elementów listy w liście jest różne od None
            for item in x:
                if item is not None:
                    suma += 1

        if tablica[0][0] == tablica[0][1] == tablica[0][2] and suma >= 5 and tablica[2] is not None and tablica[
            1] is not None:
            p = (-200, 200)
            q = (200, 200)
            punkty(p, q)
            return tablica[0][0]

        elif tablica[1][0] == tablica[1][1] == tablica[1][2] and suma >= 5 and tablica[0] is not None and tablica[
            2] is not None:
            p = (-200, 0)
            q = (200, 0)
            g = turtle.Turtle()
            punkty(p, q)
            return tablica[1][0]

        elif tablica[2][0] == tablica[2][1] == tablica[2][2] and suma >= 5 and tablica is not None:
            p = (-200, -200)
            q = (200, -200)
            punkty(p, q)
            return tablica[2][0]

        # w kolumnie

        if tablica[0][0] == tablica[1][0] == tablica[2][0] and suma >= 5 and tablica is not None:
            p = (-200, 200)
            q = (-200, -200)
            punkty(p, q)
            return tablica[0][0]

        elif tablica[0][1] == tablica[1][1] == tablica[2][1] and suma >= 5 and tablica is not None:
            p = (0, 200)
            q = (0, -200)
            punkty(p, q)
            return tablica[0][1]

        elif tablica[0][2] == tablica[1][2] == tablica[2][2] and suma >= 5 and tablica is not None:
            p = (200, 200)
            q = (200, -200)
            punkty(p, q)
            return tablica[0][2]
        return None

    def click(x, y):
        global kolej
        global ugh
        # które to pole
        kolumna = 0
        wiersz = 0

        if x < X + ODSTĘP:
            kolumna = 0
        elif x > X + 2 * ODSTĘP:
            kolumna = 2
        else:
            kolumna = 1

        if y < Y - 2 * ODSTĘP:
            wiersz = 2
        elif y > Y - ODSTĘP:
            wiersz = 0
        else:
            wiersz = 1

        # pole jest puste ?

        if tablica[wiersz][kolumna] != None: return

        # narysować

        kolumna_środek = (kolumna * ODSTĘP + ODSTĘP / 2) - BOK / 2
        wiersz_środek = (-wiersz * ODSTĘP - ODSTĘP / 2) + BOK / 2

        xo.penup()
        if ugh:
            xo.goto(kolumna_środek - 25, wiersz_środek - 25)
        if not ugh:
            xo.goto(kolumna_środek - 35, wiersz_środek - 60)


        if kolej == 'X':
            xo.write(xlos, font=('GB18030 Bitmap', 60))
        else:
            xo.write('O', font=('Old School Adventures', 50))
        # dodać informację x / o
        tablica[wiersz][kolumna] = kolej
        if kolej == 'O':
            kolej = 'X'
        else:
            kolej = 'O'
        if sprawdz() == 'X':
            xo.penup()
            xo.goto(-150, 0)
            time.sleep(1)
            xo.clear()
            xo.write("Wygrał(a) " + gracz_1 + "!", font=("Arial", 25))

        elif sprawdz() == 'O':
            xo.penup()
            xo.goto(-150, 0)
            time.sleep(1)
            xo.clear()
            xo.write("Wygrał(a) " + gracz_2 + "!", font=("Arial", 25))



        # sprawdź
        if sprawdz() != None:
            window.onclick(None)
            xo.penup()
            xo.goto(-150, 0)
            time.sleep(1)

            for i in range(15):
                x = random.randint(-300, 300)  # tworzenie fajerwerków w losowych miejscach
                y = random.randint(-300, 300)
                f.penup()
                f.goto(x, y)
                f.pendown()
                size = random.randint(10, 200)

                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                f.screen.colormode(255)  # umożliwia stosowanie modelu przestrzeni barw RGB
                f.color(r, g, b)

                for i in range(36):
                    f.forward(size)  # rysowanie fajerwerków w różnych rozmiarach i kolorach
                    f.backward(size)
                    f.left(10)
                    i += 1
                i += 1

            xo.penup()
            xo.goto(-285, -275)
            time.sleep(1)
            xo.write("<- Powrot na start", font=("Old School Adventures", 12))
            xo.penup()
            xo.goto(-270, -100)
            xo.write("- Wcisnij enter aby zagrac ponownie -", font=("Old School Adventures", 20))
            turtle.onkey(start, "Left")
            turtle.onkey(gra, "Return")

        a = None in tablica[0]
        b = None in tablica[1]
        c = None in tablica[2]
        if a == False and b == False and c == False and sprawdz() == None:
            window.onclick(None)
            xo.penup()
            xo.goto(-110, 0)
            time.sleep(1)
            xo.clear()
            xo.write("Remis", font=("Old School Adventures", 50))
            time.sleep(1)
            xo.penup()
            xo.goto(-285, -275)
            xo.write("<- Powrot na start", font=("Old School Adventures", 12))
            xo.penup()
            xo.goto(-270, -100)
            xo.write("- Wcisnij enter aby zagrac ponownie -", font=("Old School Adventures", 20))
            turtle.onkey(start, "Left")
            turtle.onkey(gra, "Return")
    window.onclick(click)

    def komputer(kolej):  # rekursja
        while sprawdz() is None:  # dopóki nie ma żadnych symboli po 3 w rzędzie
            a = random.randint(-300, 300)
            b = random.randint(-300, 300)
            if kolej == 'X' or kolej == 'O' and tablica[wiersz][kolumna] is None:
                time.sleep(2)  # opóźnienie w czasie
                click(a, b)
            return komputer(kolej)

wybor_trybu = str(window.textinput("Tryb gry", "Czy chcesz przejść do rozgrywki (1), czy obejrzeć grę instruktażową (2)?"))

if wybor_trybu == '1':
    gracz_1 = str(window.textinput("Nazwa gracza", "Imię pierwszego gracza (X):"))
    gracz_2 = str(window.textinput("Nazwa gracza", "Imię drugiego gracza (O):"))
elif wybor_trybu == '2':
    gracz_1 = 'komputer'
    gracz_2 = 'komputer'
    komputer(kolej)

    f = turtle.Turtle()
    f.speed(0)
    f.hideturtle()
start()
window.listen()
window.mainloop()