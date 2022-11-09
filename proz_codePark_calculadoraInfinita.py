def soma(numero1,numero2):
    soma_numero = numero1 + numero2
    return print(soma_numero)
    
def subtracao(numero1,numero2):
    sub_numero = numero1 - numero2
    return print(sub_numero)

def multiplicacao(numero1,numero2):
    mult_numero = numero1 * numero2
    return print(mult_numero)

def divisao(numero1,numero2):
    div_numero = numero1 / numero2
    return print(div_numero)

        

i =  1
while ( i != 0):
    tipoOperacao = int(input("Digite o tipo de operacão desejada.\n 1 - soma \n2 - subtração \n3 - multiplicação \n4 - divisão \n0 - Sair \n "))
    i = tipoOperacao
    if(tipoOperacao == 0):
        print("Finalizado")
        break
    elif(tipoOperacao !=1 and tipoOperacao !=2 and tipoOperacao !=3 and tipoOperacao !=4 and tipoOperacao != 0):
       print("valor incorreto! \n")
    else:
        numero1 = float(input("Digite o Primeiro Número: "))
        numero2 = float(input("Digite o Segundo Número: "))

        if(tipoOperacao == 1):
            soma = soma(numero1, numero2)
        elif(tipoOperacao == 2):
            sub = subtracao(numero1, numero2)
        elif(tipoOperacao == 3):
            mult = multiplicacao(numero1, numero2)
        elif(tipoOperacao == 4):
            div = divisao(numero1, numero2)
