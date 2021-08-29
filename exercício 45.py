#1 = Pedra, 2 = Papel, 3 = Tesoura.
from random import randint as r
from time import sleep as s
comp = r(1, 3)
print('\033[1;33m-=\033[m' * 30)
print('\033[1;36mVamos jogar Jokenpo? Já escolhi o que vou jogar, agora é a sua vez!\033[m')
print('\033[1;33m-=\033[m' * 30)

user = int(input('''\033[1;30m[ 1 ] PEDRA\033[m
\033[7m[ 2 ] PAPEL\033[m
\033[1;33m[ 3 ] TESOURA\033[m
\033[1;32mVocê escolhe = '''))

print('\033[mJO')
s(1)
print('KEN')
s(1)
print('PO!!!')
print('\033[1;33m-=\033[m' * 17)

#Usuario Perde
if user == 1 and comp == 2:
	print('\033[1;31mEu ganhei! Escolhi papel hahaha!\033[m')

elif user == 2 and comp == 3:
	print('\033[1;31mHahahah eu ganhei baby! Escolhi tesoura!\033[m')
elif user == 3 and comp == 1:
	print('\033[1;31mEu ganheiii! Escolhi pedra!\033[m')

#Computador Perde
elif user == 1 and comp == 3:
	print('\033[1;32mAaaf eu perdi! Escolhi tesoura!\033[m')

elif user == 2 and comp == 1:
	print('\033[1;32mAaaa não! Escolhi pedra, perdi!\033[m')

elif user == 3 and comp == 2:
	print('\033[1;32mEitaa, perdi! Escolhi papel!\033[m')

#Empate
elif user == comp:
	print('\033[1;33mOou ou, parece que empatamos!\033[m')

else:
	print('Algo de errado não esta certo.')
print('\033[1;33m-=\033[m' * 17)
