nota1 = float(input('Qual foi a 1 nota? '))
nota2 = float(input('Qual foi a 2 nota? '))
media = (nota1 + nota2) / 2

if media < 5:
	print(f'\nSua media foi: {media:.1f}, aluno \033[1;31mREPROVADO!\033[m')

elif 7 > media >= 5:
	print(f'Sua media foi: {media:.1f}, o aluno está em \033[1;33mRECUPERAÇÃO!\033[m')

elif media >= 7:
	print(f'Sua média foi: {media:.1f}, parabéns! O aluno foi \033[1;32mAPROVADO!\033[m')
