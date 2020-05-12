
"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média desras notas.
Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido,
este fato deve ser informado ao usuário e o programa termina.
"""

nota1 = float(input('Digite a primeira nota: \n'))
nota2 = float(input('Digite a segunda nota: \n'))

média = (nota1 + nota2) / 2

if not 0.0 <= nota1 <= 10.0:
    print('Nota inválida.')
elif not 0.0 <= nota2 <= 10.0:
    print('Nota inválida.')
else:
    print(f'A média entre a nota {nota1} e a nota {nota2} é {média}.')

