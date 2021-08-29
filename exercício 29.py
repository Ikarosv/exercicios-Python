km = int(input('Qual foi a velocidade do carro em km/h? '))
if km < 80:
	print('Você está livre!')
else:
	multa = (km - 80) * 7
	print(f'Você foi multado! Sua multa foi de R${multa:.2f}')
	