dia = int(input('Em que ano você está? '))
bi = dia % 4
if bi == 0:
	print('Você está em um ano bissexto!')
else:
	print('Você não está em um ano bissexto!')
