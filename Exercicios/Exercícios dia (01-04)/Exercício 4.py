nome= (input('Digite seu nome: '))
nota_1= float(input(f'Digite sua Nota: '))
nota_2= float(input(f'Digite sua Nota 2: '))
calc= (nota_1 + nota_2 ) / 2

if calc <=10 and calc >=8:
    print(f'{nome} Sua nota é {calc} , Você foi Excelente.')
elif calc <8 and calc >=5:
	print(f'{nome} Sua nota é {calc} , Você esta na media.')
else:
    print(f'{nome} Sua nota é {calc} ,Você foi reprovado.')
