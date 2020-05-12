"""
Leia um número real. Se for positivo imprima a raiz quadrada. Do contrário imprima o número ao quadrado.
"""

num = float(input('Digite um número: \n'))

if num > 0:
    print(f'A raiz quadrada o número {num: .0f} é{num **(1/2): .2f}')
else:
    print(f'O número {num} ao quadrado é {num * 2}')
