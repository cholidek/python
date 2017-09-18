# program, ktory obliczy ilosc liczb parzystych i nieparzystych w danym zakresie

zakres = input('Podaj zakres: ')
il_parzystych = 0
il_nieparzystych = 0
zakres = int(zakres)

for i in range(1, zakres + 1):
    if i % 2 == 0:
        il_parzystych += 1
    else:
        il_nieparzystych += 1
print(f'Ilość liczb nieparzystych: {il_nieparzystych}, ilość  liczb parzystych {il_parzystych}')

