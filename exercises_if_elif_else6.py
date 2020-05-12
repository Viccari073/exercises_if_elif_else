"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença
existente entre ambos.
"""

num1 = int(input('Escreva um número: \n'))
num2 = int(input('Esceva outro número: \n'))

dif1 = num1 - num2
dif2 = num2 - num1

if num1 > num2:
    print(f'O número {num1} é maior e a diferença entre eles é {dif1}.')
else:
    print(f'O número {num2} é maior e a diferença entre eles é {dif2}.')

