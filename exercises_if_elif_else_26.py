"""
Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores que 100.
Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta: Qual é a soma de a + b, onde a e b são
números aleatórios. Peça a resposta. Faça cinco perguntas ao aluno e mostre para ele as perguntas e as respostas corretas,
além de quantas vezes o aluino acertou.
"""

from random import randint

repeticoes = 0
acertos = 0

while repeticoes < 5:
    a = randint(1, 100)
    b = randint(1, 100)
    repeticoes += 1
    questao = int(input(f'Quanto é {a} + {b}? \nResposta: '))
    if questao == (a + b):
        print('Correto!')
        acertos += 1
    else:
        print(f'Errado! {a} + {b} = {a + b}')
print(f'\nDas 5 questões você acertou {acertos}!')

