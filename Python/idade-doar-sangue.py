print("Em que ano você nasceu?")
ano_nascimento = int(input())

idade = 2024 - ano_nascimento

#entre 2008 e 2007
if idade >= 16 and idade <= 17:
    print("Você precisa de autorização dos pais para doar sangue")
#entre 2007 e 1964
elif idade >=18 and idade <=60:
    print("Você pode doar sangue")
#entre 1963 e 1955
elif idade >= 61 and idade <=69:
    print("Para doar sangue, você precisa já ter doado anteriormente")
#superior a 2008
else:
    print("Você não pode doar sangue")
