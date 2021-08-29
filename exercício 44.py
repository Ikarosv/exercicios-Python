preco = float(input('Qual o preço do produto? R$ '))
condi = int(input('''\nQual será a forma de pagamento?

\033[1;33m[ 1 ] - Á vista(Dinheiro/cheque)
\033[1;34m[ 2 ] - Á vista no cartão
\033[1;35m[ 3 ] - 2x no cartão
\033[1;36m[ 4 ] - 3x ou mais\033[m
Qual será a forma de pagamento? '''))

if condi == 1:
	print(f'\033[1;33mTerá 10% de desconto, de R$ {preco} você pagará R$ {preco - (preco * 10 / 100):.2f}\033[m')

elif condi == 2:
	print(f'\033[1;34mTerá 5% de desconto, de R$ {preco} você pagará R$ {preco - (preco * 5 / 100):.2f}\033[m')

elif condi == 3:
	print(f'\033[1;35mR$ {preco} será dividido em 2x no cartão SEM JUROS! Você pagará R$ {preco/2:.2f} por mês.')

elif condi == 4:
	parc = int(input('Vai dividir de quantas vezes? '))
	parcela = preco +(preco * 20 / 100)
	print(f'\033[1;36mTerá 20% de juros, ficando R$ {parcela} e divido em {parc}x fica R$ {parcela / parc:.2f}\033[m')

else:
	print('\033[1;31mOPÇÃO DE PAGAMENTO INVALIDA! Tente novamente.\033[m')
