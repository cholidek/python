# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny


bok_1 = input('Podaj długość 1 boku: ')
bok_2 = input('Podaj długoś 2 boku: ')
bok_3 = input('Podaj długość 3 boku: ')

bok_1 = int(bok_1)
bok_2 = int(bok_2)
bok_3 = int(bok_3)

if (bok_1 < bok_2 + bok_3) or (bok_2 < bok_1 + bok_3) or (bok_3 < bok_1 + bok_2):
    print('Z podanych długości boków uda się narysować trójkąt.')

if (bok_1  == bok_2 == bok_3):
    print('Trójkąt jest równoboczny.')

if ((bok_1 == bok_2) and bok_2 != bok_3) or ((bok_2 == bok_3) and bok_2 != bok_1) or ((bok_3 == bok_1) and  bok_1 != bok_2):
        print('Trójkąt jest równoramieny')

if (bok_1 != bok_2) and (bok_2 != bok_3) and (bok_3 != bok_1):
    print('Trójkąt jest różnoboczny.')