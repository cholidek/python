x  = 0.35345353453534

#formatowanie stringa dla celów wyisania do 2 miejsc po przecinku, 2 rózne sposoby
#{} placeholder wkladamy tu zmienna

print(f'{x:.2f}')
print('{0:.2f}'.format(x))

z = 0.3
y = 0.1 + 0.1 + 0.1

#wypisanie sformatowanego stringa
print(f'z={z:.3f}')
print(f'y={y:.3f}')

# wychodzi False bo liczby sa zapisane w dziesietnym komputery pracuje w binarnym i tu jest przyklad takiej ktorej nie da sie przekac w formie binarnej
#mozn obejsc decimal uzywajac
print(z == y)

#dlatego jest false
print(f'z={z}')
print(f'y={y}')




