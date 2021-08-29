import random as r
from time import sleep

n = int(r.randint(0, 5))

print('\033[1;93m-=-\033[m' * 20)
print('Pensei em um número entre 0 e 5.')
print('\033[1;93m-=-\033[m' * 20)

e = int(input('Qual número você acha que eu pensei? '))

print('\n\033[1;31mPROCESSANDO...\033[m\n')

sleep(2)

print('\033[1;32m✓ PARABÉNS! Você acertou! ✓ \033[m' if e == n else '\033[1;31mXx Beeeeh, você errou! xX\033[m\n')

print(f'O número sorteado foi: {n}')
