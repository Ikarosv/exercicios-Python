#Perguntas
casa = float(input('Olá! Qual é o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você vai pagar? '))
 
# Prestação é casa / meses
prest = casa / (anos * 12)

if prest > salario * 30 / 100:
	print('Sinto muito, você não pode financiar esta casa.')
else:
	print(f'Parabéns, você podera financiar esta casa por R$ {prest:.2f} por mês!')
