# 1. sprawdź czy jest wygrana w kółko i krzyżyk
#   input: string 9 znaków x, o, n
#   znaki oznaczają pozycje wierszami od gornego

str_input = input('Podaj 9 znaków "x" oraz "o": ')

x = 'xxx'
o = 'ooo'
row1 = str_input[0:3]
row2 = str_input[3:6]
row3 = str_input[6:]
column1 = row1[0] + row2[0] + row3[0]
column2 = row1[1] + row2[1] + row3[1]
column3 = row1[2] + row2[2] + row3[2]
diagonal1 = row1[0] + row2[1]+ row3[2]
diagonal2 = row1[2] + row2[1]+ row3[0]

# str_input[3:] od 3 znaku 3 kolejne znaki
if len(str_input) == 9:
    if row1 == x or row1 == o:
        print('Wygrałeś')
    if row2 == x or row2 == o:
        print('Wygrałeś')
    if row3 == x or row3 == o:
        print('Wygrałeś')
    if column1 == x or column1 == o:
        print('Wygrałeś')
    if column2 == x or column2 == o:
        print('Wygrałeś')
    if column3 == x or column3 == o:
        print('Wygrałeś')
    if diagonal1 == x or diagonal1 == o:
        print('Wygrałeś')
    if diagonal2 == x or diagonal2 == o:
        print('Wygrałeś')
else:
    print('Podaj 9 znaków')
