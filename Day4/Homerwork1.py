# program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4

# użyć continue

for i in range(0, 21):
    if i % 4 == 0:
        continue
    print(i)

