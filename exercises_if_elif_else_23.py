"""
Calcule as raízes da equação de 2º grau. Lembrando que:
x = -b (mais ou menos) raiz quadrada de delta tudo  / 2a

onde delta = b**2 - 4ac
e ax**2 + bx + c = 0 representa uma equação do 2º.

A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem: 'Não é uma equação do 2º grau'.
- Se delta < 0 == não existe real. Impria: 'Não existe raiz.'
- Se delta == 0, existe uam raiz real. Imprima a mensagem: 'Raiz única.'
- Se delta >= 0, imprima: 'As duas raízes reais.
"""

a = int(input('Digite o coeficiente "a" da equação de 2º grau: '))
b = int(input('Digite o coeficiente "b" da equação de 2º grau: '))
c = int(input('Digite o coeficiente "c" da equação de 2º grau: '))

if a == 0:
    print('Não é uma equação do 2º grau.')
else:
    print(f'A equação é {a}x**2 + {b}x + {c} = 0')
    print('Vamos calcular as raízes: ')

delta = (b**2) - (4*a*c)

if delta < 0:
    print('Não existe raiz.')
elif delta == 0:
    print('Raiz única.')
elif delta >= 0:
    print('Existem duas taízes reais.')


x1 = (-b + delta**(1/2)) / 2*a
x2 = (-b - delta**(1/2)) / 2*a
print('As raízes da equação são {} e {}.' .format(x1, x2))

