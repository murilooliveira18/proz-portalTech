def calculadora(numero1,numero2,tipoOperacao):
    if(tipoOperacao == 1):
        resultado = numero1 + numero2
        return resultado
    elif(tipoOperacao == 2):
        resultado = numero1 - numero2
        return resultado
    elif(tipoOperacao == 3):
        resultado = numero1 * numero2
        return resultado
    elif(tipoOperacao == 4):
        resultado = numero1 / numero2
        return resultado
    elif(tipoOperacao !=1 or tipoOperacao !=2 or tipoOperacao !=3 or tipoOperacao !=4):
        return print("valor incorreto!")

 
numero1 = float(input("Digite o Primeiro Número: "))
numero2 = float(input("Digite o Segundo Número: "))
tipoOperacao = int(input("Digite o tipo de operacão desejada.\n 1 - soma \n2 - subtração \n3 - multiplicação \n4 - divisão \n "))
resultado = calculadora(numero1,numero2,tipoOperacao)
print(resultado)
