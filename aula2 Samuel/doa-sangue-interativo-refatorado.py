'''
Refatoração do programa "doa-sangue-interativo.py

Refatorar significa modificar um código não para alterar seu comportamento, mas para buscar melhorar a legibilidade do código.
'''

print('Qual sua idade?')
idade = int(input())

pode_doar = False #"flag" -- booleano (indica se algo é verdadeiro ou falso)

if idade >= 18 and idade <= 59:
    pode_doar = True
elif idade == 16 or idade == 17:
    print('Você tem autorização dos pais? (S/N)')
    resposta = input()
    if resposta == 's' or resposta == 'S':
        pode_doar = True
elif idade >= 60 and idade <= 69:
    print('Você já doou sangue anteriormente? (S/N)')
    resposta = input()
    if resposta == 's' or resposta == 'S':
        pode_doar = True
        
if pode_doar:
    print('Você pode doar sangue')
else:
    print('Você não pode doar sangue.')