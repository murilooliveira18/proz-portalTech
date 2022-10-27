quantidadeDeRodas = int(input("Digite a quantidade de rodas do veículo:"))
pesoBruto = int(input("Digite o peso bruto do veículo:"))
quantidadeDePessoas = float(input("Digite a quantidade de pessoas no veículo:"))

if quantidadeDeRodas >= 2 and quantidadeDeRodas <= 3:
    print("A melhor categoria de habilitação é a A")
elif quantidadeDeRodas == 4 and quantidadeDePessoas <= 8 and pesoBruto <= 3500:
    print("A melhor categoria de habilitação é a B")
elif quantidadeDeRodas >=4 and pesoBruto >= 3500 and pesoBruto <= 6000:
     print("A melhor categoria de habilitação é a C")
elif quantidadeDeRodas >= 4 and quantidadeDePessoas > 8:
    print("A melhor categoria de habilitação é a D")
elif quantidadeDeRodas >= 4 and pesoBruto > 6000 :
    print("A melhor categoria de habilitação é a E")
else:
    print("Você digitou dados inválidos ou não tem categoria adequada")
