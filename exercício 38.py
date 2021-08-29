#Interagindo com o usuário
n1 = int(input('\033[1;36mDigite o primeiro número: \033[m'))
n2 = int(input('\033[1;35m\nDigite o segundo número:\033[m '))
print(' ')

#Respostas do programa
if n1 > n2:
	print('O \033[1;36mprimeiro\033[m número é maior!')
elif n2 > n1:
	print('O \033[1;35msegundo\033[m número é maior!')
else:
	print('\033[1;31mNão tem valor maior,\033[1;32m os dois são iguais!\033[m')
