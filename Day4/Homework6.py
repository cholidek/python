# program wydający resztę z dostępnych monet: 5, 2, 1, 0.5, 0.2, 0.1

reszta = input('Podaj resztę z jakiej chesz wyliczyć ilość monet: ')
reszta = float(reszta)


il_piatek = 0
il_dwojek = 0
il_jedynek = 0
il_piecdziesieciogr = 0
il_dwudziestogr = 0
il_dziesieciogr = 0


while reszta >= 5:
    il_piatek += 1
    reszta -= 5

while reszta >= 2:
    il_dwojek += 1
    reszta -= 2

while reszta >= 1:
    il_jedynek += 1
    reszta -= 1

while reszta >=  0.5:
    il_piecdziesieciogr += 1
    reszta -= 0.5

while reszta >=  0.2:
    il_dwudziestogr += 1
    reszta -= 0.2

while reszta >=  0.1:
    il_dziesieciogr += 1
    reszta -= 0.1


print(f'Twoja reszta to: ilość piatek - {il_piatek}, ilość dwuzłotówek - {il_dwojek}, ilość jednozłotówek - {il_jedynek}, ilość pięćdziesięciogroszówek - {il_piecdziesieciogr}, ilość dwudziestogroszówek - {il_dwudziestogr}, ilość dziesięciogroszówek - {il_dziesieciogr}')

