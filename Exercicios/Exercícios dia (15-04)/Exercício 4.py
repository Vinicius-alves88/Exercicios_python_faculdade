import random

chances= int(input('Deseja jogar quantas vezes?: '))
vitorias= 0
perdas= 0
while chances > 0:
	print ('Jogo de Par ou Ímpar!')
	
	escolha= (input('Escolha Par ou Ímpar: ')).lower() 
	if escolha not in ['par' , 'impar']:
		print ('Escolha Invalida!')
		break
		
	num_1= int(input('Escolha um numero de 0 a 10: '))
	if num_1 <0 or num_1 >10:
		print('Escolha invalida!')
		break
	comp= random.randint (0, 10)
	soma= num_1 + comp
	resultado= 'par' if soma %2==0 else 'impar'
	if resultado == escolha:
		vitorias += 1
		print(f'Deu {soma}, Você ganhou!')
	else:
		perdas += 1
		print(f'Deu {soma}, Você perdeu!')
		
	chances -=1
	if chances ==0:
		print(f'Suas Jogadas Acabaram! (Vitorias: {vitorias} , Perdas: {perdas} )FIM DE JOGO!!')
		break
	continuar= (input(f'Você tem {chances} chances, Deseja continuar?(s/n): '))
	if continuar .lower() !='s':
		break
