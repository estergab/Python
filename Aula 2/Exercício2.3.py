PESO= float(input('Digite seu peso: '))
ALTURA= float(input('Digite sua altura: '))
IMC= (PESO / (ALTURA **2))
print(f'Seu imc é {IMC}')

ABAIXODOPESO= 18.5
PESONORMAL= 24.9
SOBREPESO= 29.9

if IMC <= ABAIXODOPESO:
    print('Abaixo do peso: Você é peso mosca!')
elif IMC >= ABAIXODOPESO and IMC <= PESONORMAL:
    print('Peso normal!')
elif IMC <= PESONORMAL and IMC <= SOBREPESO:
    print('Peso normal: Cê tá indo bem!')
elif IMC >= SOBREPESO:
    print('Sobrepeso: Hora de procurar um nutri, meu anjo!')
else:
    print('Obesidade: Bora mudar de vida!')
