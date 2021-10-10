"""
@author: Sebastian Bednarski
Korzystalem z pseudokodu przedstawionego na zajeciach wraz z kodem wysłanym w liscie 1 ulepszając go
"""
Ap=1 #podstawialem rowniez kolejno: 2,1,1,1,1 (podstawienie kolumnami)
Ak=5 #podstawialem rowniez kolejno: 5,5,3,3,2
Bp=1 #podstawialem rowniez kolejno: 1,2,2,3,3
Bk=5 #podstawialem rowniez kolejno: 5,5,4,4,4

if not (Ap < Ak and Bp < Bk):
    print('niespelniony warunek Ap < Ak lub Bp < Bk') #warunek niespełnienia: początek odcinka musi być mniejszy od końca
else: #jeśli spełni powyższy to
    if Ap <= Bp and Ak >= Bp: #sprawdzenie nachodzenia 
        if Ak >= Bk:
            C = Bk - Bp #odcinek B jest w odcinku A
        else: 
            C = Ak - Bp #stykają się lub nachodzą
    else: #przeciwny warunek nachodzenia: Bp >= Ap and Bp <= Ak
        if Ap <= Bk and Ak >= Bk:
            C = Bk - Ap #stykają się lub nachodzą
        elif Ap > Bp and Ak < Bk:
            C = Ak - Ap #odcinek A jest w odcinku B
        else:
            C = 0 #brak czesci wspolnej
    print('Dlugosc czesci wspolnej: ' + str(C))
