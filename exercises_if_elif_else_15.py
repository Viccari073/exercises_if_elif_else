"""
Faça um programa que calcule e mostre a área de um trapézio. Sabe se que:
A = (basemaior + basemenor) * altura tudo dividido por 2.

Lembre-se: a base maior e a base menor devem ser número maiores que zero.
"""

base_maior = float(input('Digite o tamanho da base maior: \n'))
base_menor = float(input('Digite o tamanho da base menor: \n'))
altura = float(input('Digite o tamanho da altura: \n'))

area = ((base_maior + base_menor) * altura) / 2

if base_maior <= 0 or base_menor <=0:
    print('As bases devem ser maiores que zero.')
elif base_maior < base_menor:
    print('A base maior deve ter um valor maior que a base menor.')
else:
    print(f'A área do trapézio é {area}')




