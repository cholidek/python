import copy

#tu jest typ zlozony
nabial = ['mleko', 'jajka', 'ser']
chemia = ['domestos', 'plyn do naczyn']
#tu sie robi referencja i dlatego nam nadpisuje wszystkie listy
zakupy_wrzesien = [nabial, chemia]
print('wrzesien: ', zakupy_wrzesien)

zakupy_pazdziernik = zakupy_wrzesien.copy()
print('pazdziernik: ', zakupy_pazdziernik)

zakupy_listopad = [x for x in zakupy_wrzesien]
print('listopad: ', zakupy_listopad)


# w kopiowani1 nie bo sringi chyba tam byly, tu sie kopiuje bo listy zostaly zdeklaroane w pamieci zakupowwrzesnia na pythontutor mozna zobaczyc wizulizacje
#bo ona sie dodała do listy chemia i dlatego wszstkie inne listy ja widza, bolisty dzialaja na wskaznikach pamieci, referancja do pamieci, adres do pamieci.
#jezeli kopiujemy liste do innej listy to jezeli zienimy obiek tzlozony to elementy inne ulegna zmianie


#tu bez gabek, deepcopy whcodzi jak najglebiej w liste i pojedynczo kazdy eleemnt bedzie wsadzal ich wartosci do takiego sameog elementu a nie wskazniki
#listy
zakupy_grudzien = copy.deepcopy(zakupy_wrzesien)

zakupy_wrzesien[1].append('gąbki')
print(zakupy_wrzesien)
print('pazdziernik:', zakupy_pazdziernik)
print('listopad:', zakupy_listopad)
print('grudzien:', zakupy_grudzien)

print(id(zakupy_wrzesien))
print(id(zakupy_pazdziernik))
print(id(zakupy_listopad))


