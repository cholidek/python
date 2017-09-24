#nadajac globa imie to robi si eona globalna wtedy, jest jeszcze nonlocal dzialoa inaczej - odnosi sie poziom wyzej jak np definiujemy funkcję
#w funkcji to wtedy wynosi nie globalnie a poziom wyzej do funkcji
imie = 'jola'

def drukuj_imiona(imie_2):
    global imie

    imie = 'ania'.capitalize()
    imie_2 = imie_2.capitalize()

    print(imie, imie_2)

drukuj_imiona('gosia')
print(imie)