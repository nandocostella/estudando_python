import datetime

ano_nasc = int(input("Digite o ano de nascimento "))
#busca o ano atual com a funcao datetime
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc

print("Sua idade é", idade, "anos")