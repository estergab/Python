#Laço de repetição 

while True:
    
    #Coleta os valores 
    num1 = int(input("Digite o primeiro número para iniciarmos nossa operação: ")) if num1.isalpha() else'Digite um número válido para continuar!' 

    num2 = int(input("Digite o segundo número da nossa operação: ")) if num2.isalpha() else 'Digite um número válido para continuar!' 

    #Seleciona uma opção
    menu= int(input('Digite o número da opção desejada:\n1- Adição\n2- Subtração \n3- Multiplicação \n4- Divisão \n0- Sair\n'))

    #condições 
    if menu == 1:
        print(f'A soma dos valores {num1} e {num2} é de:', num1 + num2)
    elif menu == 2:
        print(f'A subtração dos valores {num1} e {num2} é de:', num1 - num2)
    elif menu == 3:
        print(f'A Multiplicação dos valores valores {num1} e {num2} é de:', num1 * num2)
    elif menu == 4: 
        if num1 and num2 > 0:
            print(f'A Divisão dos valores {num1} e {num2} é de:', num1 / num2)
        else: 
            print('A divisão não pode ser executada ao utilizarmos 0 como um valor.\nDigite outro número para continuarmos!')

    #Opção de sair
    elif menu == 0:
        print('Operação encerrada!')
        break

    #Opção de sair
    else:
        print('Valor inválido! \nDigite um número inteiro para prosseguirmos')
        pass
