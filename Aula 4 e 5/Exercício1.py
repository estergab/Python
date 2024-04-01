palavra= input('Diga uma palavra aletória aí, meu chegado: ')
contapalavra= len(palavra)
contavogal= 0
vogal= 'aeiouAEIOUÁÀÉÍÓ'

for i in range(contapalavra):
    if palavra[i] in vogal:
        contavogal = contavogal + 1
print(contavogal)