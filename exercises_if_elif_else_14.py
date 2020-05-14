"""
A nota inicial de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 a 10,
respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas
mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5.
De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 4,9)
ou se foi aprovado. Faça todas as verificaçoes neessárias.
"""

notaTrabalho = float(input('Digite a nota do Trabalho de Laboratório: '))
notaAvaliacao = float(input('Digite a nota da Avaliação Semestral: '))
notaExame = float(input('Digite a nota do Exame Final:'))

media = ((notaTrabalho * 2) + (notaAvaliacao * 3) + (notaExame * 5)) / 10

if notaTrabalho < 0 or notaAvaliacao < 0 or notaExame < 0:
    print('Nota inválida')
elif notaTrabalho > 10 or notaAvaliacao > 10 or notaExame > 10:
    print('Nota inválida')
elif media == 0 or media <= 2.9:
    print(f'Com a média de {media} o aluno está reprovado.')
elif media == 3.0 or media <= 4.9:
    print(f'Com a média de {media} o aluno está de recuperação.')
else:
    print(f'Com a média de  {media} o aluno está aprovado.')

