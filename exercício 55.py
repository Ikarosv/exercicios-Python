#Variaveis.
maior = 0
menor = 0

#Pedindo o peso.
for a in range(1, 6):
	peso = float(input(f'Qual é o peso da {a}º pessoa? '))
	print(' ')
#Defininindo maior ou menor
	if a == 1:
		maior = peso
		menor = peso
	else:
		if peso > maior:
			maior = peso
		if peso < menor:
			menor = peso
print(f'O maior peso foi {maior}.')
print(f'O menor peso foi {menor}')
