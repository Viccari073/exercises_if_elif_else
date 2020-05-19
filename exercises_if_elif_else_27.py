"""
Faça um programa que receba três números e mostre-s em ordem crescente.


"""

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a < b < c:
    print(f'{a}\n{b}\n{c}')
if b < a < c:
    print(f'{b}\n{a}\n{c}')
if b < c < a:
    print(f'{b}\n{c}\n{a}')
if c < b < a:
    print(f'{c}\n{b}\n{a}')
if c < a < b:
    print(f'{c}\n{a}\n{b}')


