ANO_ATUAL = 2024

# primeiro perguntoo  ano de nascimento para calcular a idade
print('Qual o seu ano de nascimento?')
ano_nascimento = int(input())
idade  = ANO_ATUAL - ano_nascimento

print('Sua idade é', idade, 'anos.')

# # também posso escrever 16  <= idade <= 59
# if idade >= 18 and idade <= 69:
#    print('Pode doar sangue.')
# elif idade == 16 or idade == 17:
#    print('Pode doar sangue se tiver autorização dos pais.')
# elif idade >= 60 and idade <= 69:
#    print('Pode doar sangue contanto que seja doadorjá registrado.')
# else:
#    print('Não é possível doar sangue com essa idade')