palavra= input('Digite uma palavra, meu anjo: ')
letras= len(palavra)

for i in range(letras):
    print({i})
    inversao= letras - i
    print(palavra [inversao - 1])


#i= posição, voltas
#letras não é alterado, não reduz a posição dela de fato. Na verdade a cada volta[i] a quantidade de letras se mantém a mesma, mas a posição de verificação é alterada.
    