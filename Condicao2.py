
login= 'terezinha@gmail.com'
senha= 1234


for i in range(3):
    ten_login= input('\n Digite seu email para cadastro: ').replace(' ', '')
    if login in '@' or '.com' is False:
            print('\n Endereço de email inválido!')
    if ten_login in login:
        print('Estamos quase lá!')
        ten_senha= print(input('\n Digite sua senha: '))
        if ten_senha in senha:
            print(f'\n Bem-vindo, corno! Sua senha é:{senha}!')
        else:
             print('Tá banido!')
    else:
         print('Tá banido!')
         

