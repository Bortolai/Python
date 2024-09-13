print("Qual seu nome?")
nome = input()

print("Qual seu sobrenome?")
sobrenome = input()

print("Olá, ", nome, sobrenome)

print("Em que ano você nasceu?")
ano_nascimento = int(input())

idade = 2024 - ano_nascimento
print("Sua idade é no máximo", idade)

if ano_nascimento >= 1901 and ano_nascimento <= 2000:
    print("Você nasceu no século XX.")
elif ano_nascimento >= 2001 and ano_nascimento <= 2100:
    print("Você nasceu no século XXI.")
else:
    print("...sério?")

    #idade = 2024 - ano_nascimento
    #print("Sua idade é no máximo", idade, "anos")