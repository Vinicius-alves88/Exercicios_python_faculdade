num1 = int (input('Digite um numero:'))
num2 = int (input('Digite outro numero:'))

soma = num1 + num2

if soma %2 == 0:
    print(f'O resultado {soma}, portanto é par')
else:
    print(f'O resultado é {soma}, então é impar')
