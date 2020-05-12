"""
Faça um porgrama que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizano-se as segiuntes fórmulas (onde h corresponde à altura):

- Homens: (72.7 * h) -58
- Mulheres: (62.1 * h) - 44.7
"""

sexo = input('Qual seu sexo? \n')
h = float(input('Qual sua altura? \n'))


homem = float((72.7 * h) - 58)
mulher = float((62.1 * h) - 44.7)


if sexo == 'masculino' or 'Masculino' or 'M':
    print(f'Seu peso ideal é: {homem: .2f}')
elif sexo == 'feminino' or 'Feminino' or 'F':
    print(f'Seu peso ideal é: {mulher: .2f}')
else:
    print('Sexo inválido')


