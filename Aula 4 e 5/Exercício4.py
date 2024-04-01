palavra = input('Digite uma palavra, benzinho: ')
contador = len(palavra)
ajuste = ''

for i in range(contador):
    resultado=contador-i -1
    ajuste = ajuste + palavra[resultado]
    
if ajuste == palavra:
    print(f'A palavra {palavra} é um palíndromo')
else:
    print(f'A palavra {palavra} não é um palíndromo')

print(ajuste)

