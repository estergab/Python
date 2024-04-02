conta= '1234'
senha= '4321'
saldo= float('500.0')
ten_conta= input('Digite o número da sua conta: ') 
ten_senha= input('Digite a senha: ')

while ten_conta != conta and ten_senha != senha:
    print('Conta ou senha inválidos. Tente novamente!')
    ten_conta= input('Digite o número da sua conta: ') 
    ten_senha= input('Digite a senha: ')

while ten_conta == conta and ten_senha == senha:
    menu= int(input('Bem vindo!\n Selecione uma das opções abaixo:\n 1 - Ver saldo \n 2 - Sacar \n 3 - Fazer um depósito \n 0- Sair \n'))
    if menu == 0:
        break
    if menu == 1:
        print(f'Seu saldo é de {saldo}')
    elif menu == 2:
        input('Digite o valor que deseja sacar: ')
    elif menu == 3: 
        input('Digite o valor que deseja depositar: ')
    elif menu == 0:
        print('Este atendimento foi encerrado.')
    else:
        print('Opção inválida!')
        menu= int(input('Bem vindo!\n Selecione uma das opções abaixo:\n 1 - Ver saldo \n 2 - Sacar \n 3 - Fazer um depósito \n 0- Sair \n'))

print('Volte sempre!')
