"""
Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:

IMC                Classificação
<18,5              Abaixo do peso
18,6 a 24,9        Saudável
25,0 a 29,9        Peso em excesso
30,0 a 34,9        Obesidade grau I
35,0 a 39,9        Obesidade grau II (severa)
>= 40,0            Obesidade grau III (mórbida)
"""

peso = float(input('Digite seu peso (em kg): '))
altura = float(input('Digite sua altura (em metros):'))

imc = peso / (altura * altura)

if imc <= 18.5:
    print(f'Seu imc é{imc: .2f} e portanto você está abaixo do peso.')
elif 18.6 <= imc <= 24.9:
    print(f'Seu imc é{imc: .2f} e portanto você está saudável.')
elif 25.0 <= imc <= 29.9:
    print(f'Seu imc é{imc: .2f} e portanto você está com peso em excesso.')
elif 30.0 <= imc <= 34.9:
    print(f'Seu imc é{imc: .2f} e portanto você está com obesidade grau I.')
elif 35.0 <= imc <= 39.9:
    print(f'Seu imc é{imc: .2f} e portanto você está com obesidade grau II (severa).')
else:
    print(f'Seu imc é {imc} e portanto você está com obesidade grau III (móbida)).')
