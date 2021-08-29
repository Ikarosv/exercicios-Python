#Pedindo os números
b = 0
for n in range(1, 7):
	a = int(input('Digite um valor: '))
	print(' ')
	if a % 2 == 0:
		b += a
if b > 1:
	print(f'A soma dos número pares são: {b}.')
else:
	print('Parece que você não colocou nenhum número par.')
