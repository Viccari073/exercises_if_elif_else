"""
Faça um programa que receba um número e verifique se este número é par ou ímpar.
"""

num = int(input('Escreva um número:'))

if (num/2) == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é ímpar.'.format(num))
