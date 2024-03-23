Operacao= None

while Operacao != 0:
    Operacao= int(input('Vamos fazer uma continha! Escolha uma operação: \n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 0 - Sair \n'))
    if Operacao == 1:
        NumI= int(input('Digite o primeiro número da nossa operação: '))
        NumII= int(input('Digite o segundo número da nossa operação: '))
        Result= NumI + NumII
        print(f'O resultado da soma é: {Result}')
    elif Operacao == 2:
        NumI= int(input('Digite o primeiro número da nossa operação: '))
        NumII= int(input('Digite o segundo número da nossa operação: '))
        Result= NumI - NumII
        print(f'O resultado da subtração é: {Result}')
    elif Operacao == 3:
        NumI= int(input('Digite o primeiro número da nossa operação: '))
        NumII= int(input('Digite o segundo número da nossa operação: '))
        Result= NumI * NumII
        print(f'O resultado da multiplicação é: {Result}')
    elif Operacao == 4:
        NumI= int(input('Digite o primeiro número da nossa operação: '))
        NumII= int(input('Digite o segundo número da nossa operação: '))
        Result= NumI / NumII
        print(f'O resultado da divisão é: {Result}')
    elif Operacao > 4:
        print('Opção invalida, meu anjo! É só 1, 2, 3, 4 ou 0')
print('Acabou, vá estudar desgraça!')





#print(input('Olá, vamos fazer uma continha? Encolha entre:\n 1-Adição \n')) 
#Adição= None
#Sub= None
#Mult= None
#Divisão= None