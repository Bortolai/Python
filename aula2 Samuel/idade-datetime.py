import datetime

data = datetime.datetime.now() # data de AGORA, incluindo ano, mês, ..., até milissegundos
ano_atual = data.year # pego apenas o campo YEAR (ano) da data atual

print('Em que ano você nasceu?')
ano_nascimento = int(input())
print('Em que mês você nasceu?')
mes_nascimento = int(input())
print('Em que dia você nasceu?')
dia_nascimento = int(input())

idade =  data.year - ano_nascimento

if (data.month, data.day) < (mes_nascimento, dia_nascimento):
    idade -= 1

print('Sua idade é: ', idade, 'anos')

# print('Estamos no ano', ano_atual)
# print('Portanto você fez ou fará', idade, 'anos neste ano.')
# idade =  ano_atual - ano_nascimento

# Exercício para sexta- feira
#  Perguntar o dia e mês de nascimento do usuário
# Descobrir

