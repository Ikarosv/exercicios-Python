n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))
n3 = int(input('Digite o número 3: '))
print('\n')
#Menor Número
menor = n1
if n2 < n1 and n2 < n3:
	menor = n2

if n3 < n1 and n3 < n2:
	menor = n3

print(f'O menor número é: {menor}!')

#Maior Número
maior = n1
if n2 > n1 and n2 > n3:
	maior = n2

if n3 > n1 and n3 > n2:
	maior = n3
	
print(f'O maior número é: {maior}!')
