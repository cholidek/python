
def drukuj_kwadraty():
    liczby = range(8,15)
    for l in liczby:
        print(l**2)
drukuj_kwadraty()

# x = drukuj_kwadraty()
# #none sie dopisze dlatego bo x=drukuj_kwadraty i wykonujemy x nie dostal wartosci i dlatego ten none - zmienna istnieje ale nie ma wartosci
# print(x)
# #x jest zadnym typem
# print(type(x))
#
# #tu odwolasnie do funkcji przypisanej do x, roznica pomiedzy wywowalniem funkjci to ()
# x()



def drukuj_kwadraty(od, do):
    for l in range(od, do+1):
        print(l**2)

drukuj_kwadraty(2,15)
#błędne wywołąnie funkcji
# drukuj_kwadraty(7)
# drukuj_kwadraty(2,5,6)
