#Interagindo com o usuário.
numero = int(input('Qual é o número a ser convertido? '))
modo = int(input('''Qual o modo de conversão?

\033[1;33m1 - Binário
\033[1;31m2 - Octal
\033[1;34m3 - Hexadecimal\033[m]
R = '''))

#Cálculo e Condições
if modo == 1:
	print(f'O número: {numero} convertido em \033[1;33mbinário \033[mé: \033[1;33m{numero:b}')
elif modo == 2:
	print(f'O número: {numero} convertido em \033[1;31moctal \033[mé: \033[1;31m{numero:o}')
elif modo == 3:
	print(f'O número: {numero} convertido em \033[1;34mhexadecimal\033[m é: \033[1;34m{numero:x}')
else:
	print('Opção invalida! Tente novamente.')
