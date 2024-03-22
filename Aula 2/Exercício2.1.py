numero1= int(input('Digite um número: '))

if numero1 < 0:
    print(f'{numero1} é negativo')
elif numero1 > 0:
    print(f'seu número é positivo')
elif numero1 == 0:
    print(f'seu número é igual a 0')