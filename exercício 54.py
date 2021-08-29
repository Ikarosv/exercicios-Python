from datetime import date
atual = date.today().year
b = 0
c = 0
for a in range(1, 8):
	ano = int(input(f'Qual o ano de nascimento da {a}º pessoa? '))
	print(' ')
	nasc = atual - ano
	if nasc < 21:
		b += 1
	elif nasc >= 21:
		c += 1
print(f'{b} pessoas ainda são menores, e {c} pessoas já são maiores.')
