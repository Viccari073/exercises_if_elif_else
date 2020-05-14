"""
Dados três valores, A, B e C. Verificar se eles podem ser valores dos lados de um triângulo e, se forem,
se pe um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:

- O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
- Chama-se equilátero o triângulo que tem os três lados iguais.
- Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
- Recebe o nome de escaleno o triângulo que tem três lados diferentes.
"""

A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))
C = int(input('Digite o valor de C: '))

if A+B < C or A+C < B or B+C < A:
    print('Não corresponde a um triângulo.')
elif A == B and A == C and B == C:
    print('Os valores correspondem a um triângulo equilátero.')
elif A == B != C or A == C != B or B == C != A:
    print('Os valores correspondem a um triângulo isósceles.')
elif A != B and A != C and B != C:
    print('Os valores correspondem a um triângulo escaleno.')







