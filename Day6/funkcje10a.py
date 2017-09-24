def dodaj_imie(imie, imiona = None):
    if imiona == None:
        imiona = []
    imiona.append(imie)
    return imiona

baza  = dodaj_imie('Marta')
dodaj_imie('Marek', baza)

print(baza)

anglicy = dodaj_imie('Jhon')
print(anglicy)

def policz(a,b):
    #zwracamy ponizej tupla z 2 wartosciai bo okragle nawiasy, zwrocenie 2 wartosci naraz
    return (a**2, b**3)
x,y = policz(3,4)
print(x)
print(y)



