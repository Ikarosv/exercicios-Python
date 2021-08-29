sl = float(input('Qual o salário? R$ '))

if sl > 1250.00:
	aumento = float(sl + (sl * 0.1) )
if sl <= 1250.00:
	aumento = float(sl +(sl * 0.15))

print(f'Aumento de: R$ {aumento:.2f}')
