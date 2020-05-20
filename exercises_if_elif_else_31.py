"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número.
Isto é, domingo se 1, segunda-feira se 2 e assim por diante.
"""
# Resolução do professor:

"""

def switch(valor):
    switcher = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado",
    }
    return switcher.get(valor, "Não encontei o dia correspondente.")


dia = int(input('Informe um número referente a um dia da semana: '))

print(switch(dia))
"""

dia = int(input("Informe um número referente ao um dia da semana:\n"))

if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda-feira')
elif dia == 3:
    print('Terça-feira')
elif dia == 4:
    print('Quarta-feira')
elif dia == 5:
    print('Quinta-feira')
elif dia == 6:
    print('Sexta-feira')
elif dia == 7:
    print('Sabado')
else:
    print('Esse dia não existe')
