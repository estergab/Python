import random
numero= random.randrange (1, 100)
contador = 0
tentativas = 0 
numerouser= int(input('Tente acertar em qual número estou pensando: '))

while numero != numerouser:
    if numerouser < numero:
        print('Digite um número maior: ')
    elif numerouser > numero:
        print('Digite um número menor')
    tentativas = tentativas +1
    numerouser= int(input('Tente acertar em qual número estou pensando: '))
print(f'Parabéns, você acertou! Número de tentativas foi: {tentativas}')

