
try:
    x= int(input('Digite o primeiro número da nossa operação: '))
    y= int(input('Digite o segundo número da nossa operação: '))
except ValueError :
    print('\nO Valor informado não é um número inteiro. Tente novamente!')
    pass 

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    return x / y

def mult(x, y):
    return x * y


while True:
    menu= int(input('Digite o número de uma das opções:\n1- Soma \n2- Subtração \n3- Divisão \n4- Multiplicação \n0- Sair\n'))

    if menu == 1:
        print(soma(x,y))
    
    elif menu ==2:
        print(sub(x,y))

    elif menu ==3:
        print(div(x,y))

    elif menu ==4:
        print(mult(x,y))

    elif menu == 0:
        print('Até a próxima!')
        break

    else:
        print('\nO Valor informado não é um número inteiro. Tente novamente!')