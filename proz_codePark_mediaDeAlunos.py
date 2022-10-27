nomeAluno = input("Escreva seu nome: ")
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
faltas = int(input("Digite a quantidade de faltas:"))
media = (nota1 + nota2 / 2)

if media < 7 :
    print(nomeAluno , " você foi reprovado com uma média:" , media)
else:
    print(nomeAluno , " você foi aprovado com uma média:" , media)

if faltas >= 3 :
    print(nomeAluno , " você foi reprovado com um número de faltas:" , faltas)
else:
    print(nomeAluno , " você foi aprovado com um número de faltas:" , faltas)

