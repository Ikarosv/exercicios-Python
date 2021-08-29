peso = float(input('Olá! Qual é seu peso? '))
altur = float(input('E a sua altura? '))
imc = peso / (altur * altur)
print(f'\033[1;36mSeu Índice de Massa Corporea é: \033[7m{imc:.1f}\033[m')

if imc < 18.5:
	print('\033[1;33mVocê está abaixo do peso. Cuidado!\033[m')

elif imc > 18.5 and imc < 25:
	print('\033[1;32mVocê está no peso ideal, muito bem!\033[m')

elif imc >= 25 and imc < 30:
	print('\033[1;33mVocê está um pouquinho acima do peso ideal\033[m')

elif imc >= 30 and imc < 40:
	print('\033[1;33mVocê está em situação de obesidade!\033[m')

elif imc > 40:
	print('\033[1;41mVocê está em situação de obesidade mórbida! É recomendavel procurar um médico!\033[m')
