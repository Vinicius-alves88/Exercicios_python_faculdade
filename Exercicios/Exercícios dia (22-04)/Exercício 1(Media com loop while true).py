while True:
	nome= (input('Nome do aluno: '))
	nota1= (int(input('Digite sua primeira nota: ')))
	nota2= (int(input('Digite sua segunda nota: ')))
	media= nota1 + nota2 // 2
	print (f'A media do aluno {nome} é {media}.')
	if media >=7:
		print ('O ALUNO FOI APROVADO!')
	else:
		print ('O ALUNO FOI REPROVADO!')
	continuar= (input('Deseja saber a nota de outro aluno? (s/n): '))
	if continuar !='s':
		break
	
