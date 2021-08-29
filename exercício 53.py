'''palavra = str(input('Digite uma frase: '))
palavra = palavra.replace(' ', '')
palavra = palavra.lower()
pala = palavra[::-1]
if pala == palavra:
	print('É')
else:
	print('Não é')'''

#Com o for:
frase = str(input('Digite uma frase: ')).strip().upper().split()
junto = ''.join(frase)
inverso = ''
for letra in range(len(junto) - 1, - 1, -1):
	inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
	print('É um palindromo!')
else:
	print('Não é um palindromo!')

