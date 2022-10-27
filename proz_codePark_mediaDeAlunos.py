nomeAluno = input("Escreva seu nome: ")
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
faltas = float(input("Digite a quantidade de faltas:"))
media = float(nota1 + nota2 / 2)

if media <= 7 or faltas > 3: 
    print(nomeAluno + " você foi reprovado")
else:
    print(nomeAluno + " você foi aprovado")

