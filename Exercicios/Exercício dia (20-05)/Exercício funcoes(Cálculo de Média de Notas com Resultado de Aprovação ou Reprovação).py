def dignom():
	nome= (input('Digite o nome do aluno: '))
	return nome
	
def notass():
	a = float(input('Digite sua Primeira Nota: '))
	b = float(input('Digite sua Segunda Nota: '))
	c = float(input('Digite sua Terceira Nota: '))
	resultado = (a + b + c) / 3
	return resultado

def process():
	nome= dignom()
	calc= notass()
	print(f'A media do aluno {nome} é {calc}')
	if calc >=7:
		print(f'Você passou!!')
	else:
		print('Você foi reprovado!!')
	return
	
d= process()
print(d)
