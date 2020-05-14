"""
Ler um número inteiro. Se o número lido for negaivo, escreva a mensagem: Número inválido".
Se o número for positivo, calcular o logaritmo desse número.
"""

from math import log

num = int(input('Digite um número: '))

if num < 0:
    print('Número inválido')
else:
    print(f'O logarítmo de {num} é: {log(num)}')
