"""
Faça um programa que receba a altura e o peso de uma pessoa.
De acordo com a tabela abaixo, verifique e mostre qual a classificação dessa pessoa:

    Altura                             Peso
                      até 60        entre 60 e 90       acima de 90
menor que 1.20          A                D                  G
de 1.20 a 1.70          B                E                  H
maior que 1.70          C                F                  I



"""

altura = float(input("Digite a altura: "))
peso = float(input('Digite o peso: '))

if altura < 1.20 and peso < 60:
    print(f'Você é da classe A')
elif altura < 1.20 and 60 <= peso <= 90:
    print(f'Você é da classe D')
elif altura < 1.20 and peso > 90:
    print(f'Você é da classe G')
elif (1.20 <= altura <= 1.70) and peso < 60:
    print(f'Você é da classe B')
elif (1.20 <= altura <= 1.70) and (60 <= peso <= 90):
    print(f'Você é da classe E ')
elif (1.20 <= altura <= 1.70) and peso > 90:
    print(f'Você é da classe H')
elif altura > 1.70 and peso < 60:
    print(f'Você é da classe C')
elif (altura > 1.70) and (60 <= peso <= 90):
    print(f'Você é da classe F')
else:
    print(f'Você é da classe I')
