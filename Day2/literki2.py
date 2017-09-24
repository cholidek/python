#slicowanie
slowo = 'czarymary'


#ostatnia litera wydrukowana z indeksu 4
print(slowo[2:5])

#python zacznie od 0 indeksu
print(slowo[:5])
print(slowo[2:])

print(slowo[2:7:2])

#kod ASCII zamienia literkę na kod ASCII
kod = ord('D')
print(kod)

#stoisz na funkcji kursorem ctrl+q pokazuje pomoc

# odwrotnie do funkcji ord zamienia wynik ASCII na literkę
print(chr(kod+4))

# błąd poza zakresem out of range
s = 'kotek'
#s[5]
#s[-6]
#s[0:4:2]- bierze co 2 litere z zakresu 0:4
#s[::] - drukuje cały zakres od początku do końca z krokiem jeden
#s[::-1] - od końca do początku co jeden
print(s)
