#Descobrindo a idade do atleta.
from datetime import date
atual = date.today().year
ano = int(input('Qual o ano de nascimento do atleta? '))
idad = atual - ano
print(f'Idade do atleta: {idad}')

#Classificando o atleta.
if idad <= 9:
	print('\033[1;32mClassificaçao do atleta:\033[1;34m MIRIM!\033[m')

elif idad > 9 and idad <= 14:
	print('\033[1;32mClassificaçao do atleta:\033[1;34m INFANTIL!\033[m')

elif idad > 14 and idad <= 19:
	print('\033[1;32mClassificaçao do atleta:\033[1;34m JUNIOR!\033[m')

elif idad == 20:
	print('\033[1;32mClassificaçao do atleta:\033[1;34m SENIOR!\033[m')

elif idad > 20:
	print('\033[1;32mClassificaçao do atleta:\033[1;34m MASTER!\033[m')
