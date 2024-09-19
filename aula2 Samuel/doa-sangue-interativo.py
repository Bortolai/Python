print('Qual sua idade?')
idade = int(input())

if idade >= 70 or idade < 16:
    print('Não pode doar sangue.')
elif idade == 16 or idade == 17:
    print('Você tem autorização dos pais? (S/N)')
    resposta = input()
    if resposta == 's' or resposta == 'S':
        print('Pode doar sangue.')
    else:
        print('Não pode doar sangue.')
elif idade >= 60 and idade <= 69:
    print('Você já doou sangue anteriormente? (S/N )')
    resposta = input()
    if resposta == 's' or resposta == 'S':
        print('Pode doar sangue.')
    else:
        print('Não pode doar sangue.')
else:
    print('Pode doar sangue.')