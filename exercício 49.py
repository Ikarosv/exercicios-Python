#Pedindo o Número
num = int(input('Escolha um número para mostrar a tabuada: '))

#Criando a Tabuada.
print('\033[1;33m—\033[m' * 12)
for a in range(1, 11):
	print(f'{num} × {a} = {num * a}')
print('\033[1;33m—\033[m' * 12)
