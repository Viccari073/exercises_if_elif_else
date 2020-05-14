"""
Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou por 5. mas nõa
simultaneamente pelos dois.
"""

num = int(input('Digite um número: '))

if num % 3 == 0 and num % 5 == 0:
    print(f'Número simultaneamente divido por 3 e 5.')
elif num % 3 == 0:
    print(f'O número {num} é divido por 3.')
elif num % 5 == 0:
    print(f'O número {num} é divido por 5.')



