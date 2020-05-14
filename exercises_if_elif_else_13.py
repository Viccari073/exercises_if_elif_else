"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas.
A primeira e a segunda tem peso 1 e a terceira tem peso 2.
Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
A nota para aprovação deve ser igual ou superior a 60 pontos.
"""

nota1 = float(input('Digite a primeira nota: \n'))
nota2 = float(input('Digite a segunda nota: \n'))
nota3 = float(input('Digite a terceira nota: \n'))

pesoNota3 = nota3 * 2

media = (nota1 + nota2 + pesoNota3) / 3

if media < 60:
    print('Aluno doi reprovado.')
else:
    print('Aluno foi aprovado.')
