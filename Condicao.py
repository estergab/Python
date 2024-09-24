beb_alc= 'BAC001'
beb_s_alc= 'BSA001'

codigo= input('Digite os três primeiros digitos do código do produto: ').upper().replace(' ', '')

if codigo in beb_alc:
    print(f' ----------------------------------------------------------------------\n A bebida informada é alcoolica. \n ---------------------------------------------------------------------- \n É expressamente proibida a venda dessa bebida à menores de 18 anos!\n ---------------------------------------------------------------------- \n Beba com moderação!\n')
elif codigo in beb_s_alc:
    print(f'\n A bebida informada NÃO é alcoolica!\n') 
else: 
    print('\n Produto não encontrado no estoque\n')









login= 'BAC001'
senha= 'BSA001'

codigo= input('Digite seu email para cadastro: ')\
    .replace(' ', '')\
    .replace()

if codigo in beb_alc:
    print(f' ----------------------------------------------------------------------\n A bebida informada é alcoolica. \n ---------------------------------------------------------------------- \n É expressamente proibida a venda dessa bebida à menores de 18 anos!\n ---------------------------------------------------------------------- \n Beba com moderação!\n')
elif codigo in '@' or '.com' is False:
    print('Endereço de email inválido!')
elif codigo in beb_s_alc:
    print(f'\n A bebida informada NÃO é alcoolica!\n') 
else: 
    print('\n Produto não encontrado no estoque\n')
