a = float(input('Qual o comprimento da reta 1? '))
b = float(input('Qual o comprimento da reta 2? '))
c = float(input('Qual o comprimento da reta 3? '))

if  (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
	print('Dá para formar um triângulo!')
	
	#Triângulo Eqquilátero
	if a == b == c:
		print('O triângulo será \033[1;32m Equilátero!\033[m')
	
	#Triângulo Escaleno
	elif a != b != c != a:
		print('O triângulo será \033[1;32m Escaleno!\033[m')
		
	#Triângulo Isóceles
	else:
		print('O triângulo será \033[1;32m Isóceles!\033[m')

else:
	print('Não dá para formar um triângulo!')
	print('F')
