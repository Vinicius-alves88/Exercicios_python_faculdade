nome = (input('Digite seu nome: '))
nota_1 = float(input(f'Digite sua Nota: '))
nota_2 = float(input(f'Digite sua Nota 2: '))
nota_3 = float(input(f'Digite sua Nota 3: '))
faltas = int(input(f'Digite as faltas: '))
calc = (nota_1 + nota_2 + nota_3) / 3
if calc >=7 and faltas <=5: 
    print(f'{nome} Sua nota é {calc} , Você foi aprovado.')
else:
    print(f'{nome} Sua nota é {calc} ,Você foi reprovado.')
