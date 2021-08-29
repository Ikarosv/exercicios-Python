kms = int(input('Quantos kms foi a viajem? '))
if kms <= 200:
	print(f'Vocé pagará: R${kms * 0.50:.2f}')
else:
	print(f'Você pagará: R${kms * 0.45:.2f}')