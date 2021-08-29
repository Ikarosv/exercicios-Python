from datetime import date
atual = date.today().year
nasc = int(input('Qual sua data de nascimento? '))

idade = atual - nasc

print(f'Sua idade é: \033[1;33m{idade}\033[m\n')

#Tempo que FALTA
if idade < 18:
	print('\033[1;32mAinda não está na hora de se alistar!\033[m')
	falta = 18 - idade
	ano = atual + falta
	print(f'Você irá se alistar no ano de {ano}.')
	
	#Plural ou singular
	if falta == 1:
		print('\033[1;36;41mFalta 1 ano para você se alistar, fique atento!\033[m')
	elif falta > 1:
		print(f'Faltam {falta} anos para você se alistar, pode ficar tranquilo!')

#Idade IGUAL
elif idade == 18:
	print('\033[1;33mEstá na hora de se alistar! Boa sorte Soldado!\033[m')

#Tempo que PASSOU
elif idade > 18:
	print('\033[1;31mTá doido soldado? Já passou da hora de se alistar!\033[m')
	passou = idade - 18
	ano = atual - passou
	print(f'Você deveria ter se alistado em {ano}.')
	
	#Plural ou singular.
	if passou == 1:
		print('Passou 1 ano, e você não se alistou! \033[1;41mAtenção!\033[m')
	elif passou > 1:
		print(f'Passaram-se {passou} anos! Vá se alistar, corre!')
