"""
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""

num = int(input('Escreva um número positivo ou negativo: \n'))

if num >= 0:
    print(f'A raiz quadrada desse número é {num**(1/2): .0f}')
else:
    print('Esse número é inválido.')

