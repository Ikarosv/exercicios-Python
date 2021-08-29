a = float(input('Qual o comprimento da reta 1? '))
b = float(input('Qual o comprimento da reta 2? '))
c = float(input('Qual o comprimento da reta 3? '))

if  (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
	print('Dá para formar um triângulo!')

else:
	print('Não dá para formar um triângulo!')
	print('F')
