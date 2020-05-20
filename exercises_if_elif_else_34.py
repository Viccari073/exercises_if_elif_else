"""
Leia a nota e p número de faltas de um aluno, e escreva seu conceito.
Se acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.

Nota             Conceito até 20 faltas              Conceito com mais de 20 faltas
9.0 até 10.0               A                                       B
7.5 até 8.9                B                                       C
5.0 até 7.4                C                                       D
4.0 até 4.9                D                                       E
0.0 até 3.9                E                                       E
"""

print('Qual a nota do aluno?')
nota = float(input())

print('Quantas faltas ele teve?')
faltas = int(input())

if 9.0 <= nota <= 10 and faltas < 20:
    print(f'O aluno tem o conceito A')
elif 9.0 <= nota <= 10 and faltas > 20:
    print(f'O aluno tem o conceito B')

if 7.5 <= nota <= 8.9 and faltas < 20:
    print(f'O aluno tem o conceito B')
elif 7.5 <= nota <= 8.9 and faltas > 20:
    print(f'O aluno tem o conceito C')

if 5.0 <= nota <= 7.4 and faltas < 20:
    print(f'O aluno tem o conceito C')
elif 5.0 <= nota <= 7.4 and faltas > 20:
    print(f'O aluno tem o conceito D')

if 4.0 <= nota <= 4.9 and faltas < 20:
    print(f'O aluno tem o conceito D')
elif 4.0 <= nota <= 4.9 and faltas > 20:
    print(f'O aluno tem o conceito E')

if 0.0 <= nota <= 3.9 and faltas < 20:
    print(f'O aluno tem o conceito E')
elif 0.0 <= nota <= 3.9 and faltas > 20:
    print(f'O aluno tem o conceito E')