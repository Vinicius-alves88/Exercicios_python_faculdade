import random
vidas= 3
matou= 0
while vidas >0:
	atirar= (input('Deseja atirar? (s/n): '))
	comp= random.choice (['Morreu', 'Errou', 'Matou'])
	if comp == 'Morreu':
		vidas -=1
		print (f'Você morreu!')
		print(f'Você tem {vidas} Vidas!!')
	elif comp == 'Errou':
		print(f'Você errou!')
		print(f'Você tem {vidas} Vidas!!')
	else:
		print(f'Você matou!')
		print(f'Você tem {vidas} Vidas!!')
		matou +=1
	if vidas == 0:
		print (f'Você matou({matou}) vezes!')
