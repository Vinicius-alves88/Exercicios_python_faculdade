import random
print ('Jogo de Pedra, Papel ou Tesoura')
jog= str(input('Escolha Pedra, Papel ou Tesoura: '))

comp= random.choice(['Pedra', 'Papel',' Tesoura'])
print (f'Você escolheu {jog}.')
print(f'O computador escolheu {comp}.')

if jog == comp:
	print ('Deu empate!')
elif jog == 'Pedra' and comp == 'Tesoura':
	print ('Você venceu!')
elif jog == 'Papel' and comp == 'Pedra':
	print ('Você venceu!')
elif jog == 'Tesoura' and comp == 'Papel':
	print ('Você venceu!')
else:
	print ('Você perdeu!')
