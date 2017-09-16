# elif

x = int(input('Podaj liczbę całkowitą x:'))
y = int(input('Podaj liczbę całkowitą y:'))


#
if x == y:
    print('liczby są równe')

#
if x > 5:
    x +=1
    print('x jest równy', x)
elif x == 3:
    x *= 2
    print('x jest równy', x)

print('koniec programu')

# x+=1 => x = x+1
# x *= => x = x*2
# działą też dla \= dzielenia i odejmowanie -=