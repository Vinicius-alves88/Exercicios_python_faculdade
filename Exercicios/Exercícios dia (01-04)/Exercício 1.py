num1= int(input('Digite um Numero: '))
num2 = int(input('Digite outro Numero: '))

soma= num1 + num2
print (f'O resultado da soma é {soma}.')
mult= num1 * num2
print (f'O resultado da multiplicação é {mult}.')
div= num1 // num2
print (f'O resultado da divisão é {div}.')
pot= num1 ** num2
print (f'O resultado da potenciação é {pot}.')

calc= (soma + mult + pot + div)**2

if calc %2 == 0:
    print(f'O resultado elevado ao quadrado é {calc}, esse numero é par')
else:
    print(f'O resultado é elevado ao quadrado é {calc}, esse numero é impar')
