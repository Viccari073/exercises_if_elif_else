"""
Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:

Categoria      Idade
Infantil A     5 a 7
Infantul B     8 a 10
Juvenil A      11 a 13
Juvenil B      14 a 17
Sênior         maiores de 18

"""

idade = int(input('Qual a idade do nadador? \n'))

if 5 <= idade <= 7:
    print('Com a idade de {} anos, o nadador é da categoria Infantil A'.format(idade))
elif 8 <= idade <=10:
    print('Com a idade de {} anos, o nadador é da categoria Infantil B'.format(idade))
elif 11 <= idade <= 13:
    print('Com a idade de {} anos, o nadador é da categoria Juvenil A'.format(idade))
elif 14 <= idade <= 17:
    print('Com a idade de {} anos, o nadador é da categoria Juvenil B'.format(idade))15
elif idade >= 18:
    print('Com a idade de {} anos, o nadador é da categoria Senior'.format(idade))
else:
    print('Com a idade de {} anos, o nadador é muito novo para competir.'.format(idade))


