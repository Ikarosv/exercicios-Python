s = 0
cont = 0
for c in range(3, 501, 6):
	s += c
	cont += 1
print(f'A soma entre os {cont} valores divisiveis por 3 é: {s}')

#Ou também pode ser:
con = 0
sum = 0
for a in range(1, 501, 2):
	if a % 3 == 0:
		sum += a
		con += 1
print(f'\nDo outro modo {sum} a soma é {con} a contagem')
