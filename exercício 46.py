from time import sleep as s
from emoji import emojize as e

for c in range(10, 0, -1):
	print(f'\033[1;36m{c:-^60} \033[m')
	s(1)
print(e('\033[1;33mFeliz Ano Novo!\033[m' + ':fireworks: ' * 10))
