nome = input("Qual seu nome?")
while True:
    try:
        anoNascimento = int(input("Qual o ano que você nasceu? (data deve ser entre 1992 até 2021) "))
        if anoNascimento >= 1992 and anoNascimento <= 2021:
            idade = 2022 - anoNascimento
        print(nome, "você completa", idade, "anos de idade em 2022")
        break
    except:
            print("Ano digitado é fora do limite permitido.")

