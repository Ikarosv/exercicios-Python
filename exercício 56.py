#Variaveis
media = 0
maiori = 0
velho = 'a'
nfem = 0
#1º Pedir o nome, idade e sexo 4 vezes.
for vezes in range(1, 5):
	print(f'------ {vezes}º Pessoa ------')
	nome = str(input('Nome: '))
	idade = int(input('Idade: '))
	sexo = str(input('Sexo [M/F]: ')).upper()
	#2º Media de idade.
	media += idade
	#3º Homem mais velho.
	if vezes == 1:
		if sexo == 'M':
			maiori = idade
			velho = nome
	elif sexo == 'M' and idade > maiori:
		maiori = idade
		velho = nome
	#4º Contagem de mulheres abaixo de 20.
	if sexo == 'F' and idade < 20:
		nfem += 1
#Prints fora do laço
print(f'\nA media das idades é: {media/4}')
print(f'O homem mais velho é {velho.upper()} com {maiori} anos')
print(f'{nfem} mulheres tem menos de 20')
