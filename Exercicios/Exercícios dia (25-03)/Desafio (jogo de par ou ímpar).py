import random

while True:
    escolha= (input('Escolha par ou impar: '))
    num_1= int(input('Escolha um Numero de 0 a 10: '))
    
    if escolha not in ['par','impar']:
    	print('Escolha invalida.')
    	
    if num_1 < 0 or num_1 > 10:
    	print('Número inválido. Por favor, escolha um numero de 0 a 10: ')
    	
    computador_num = random.randint(0, 10)
    
    print(f'Você escolheu {num_1} e o computador escolheu {computador_num}')
    
    soma= num_1 + computador_num
    
    resultado= 'par' if soma %2==0 else 'impar'
    
    if resultado == escolha:
    	print(f'Deu {soma}, Você ganhou!')
    else:
    	print(f'Deu {soma}, Você perdeu! Tente novamente.')
    	
    continuar= (input('Deseja continuar? (s/n): '))
    if continuar .lower() !='s':
    	break
