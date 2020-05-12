"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:

- O número digitado ao quadrado
- A raiz quadrada do número digitado

"""

num = int(input("Digite um número: \n"))

if num > 0:
    print(f'O número {num} ao quadrado é {num *2}')
    print(f'A raiz quadrada do número {num} é {num **(1/2): .2f}')
else:
    print()
