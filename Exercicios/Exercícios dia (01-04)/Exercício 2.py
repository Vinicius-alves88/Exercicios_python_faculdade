nome= str(input('Digite seu nome: '))
idade= int(input('Digite sua idade: '))

if idade >=18:
	print(f'Você tem {idade}, então você é obrigado a votar.')
elif idade ==16 or 17:
	print(f'Voce tem {idade}, Seu voto é opcional.')
else:
	print(f'Você tem {idade}, Você não é obrigado a votar.')
