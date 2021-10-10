"""
@author: Sebastian Bednarski
"""
boki = [3, 4, 5] #sprawdzenie warunku a
#boki = [3, 10, 5] #sprawdzenie warunku b
o_pol = (boki[0] + boki[1] + boki[2]) / 2 #p do wzoru herona

iloczyn = o_pol
for i in range(len(boki)):
    iloczyn *= (o_pol - boki[i])

pole = iloczyn** 0.5 #pierwiastek
if ((boki[0] + boki[1]) > boki[2] and (boki[0] + boki [2]) > boki[1] and (boki[1] + boki[2]) > boki[0]): #warunek powstania trójkątów
    print('Pole wynosi: ' + str(pole)) #poprawny warunek
else:
    print('Nie ma spelnionego warunku powstania trojkata') #niespełniony warunek