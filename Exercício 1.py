nome = input("Qual o seu nome? \n")
idade = int(input("Agora digite sua idade: \n"))
altura = float(input("Por fim, qual sua altura? \n"))

print(f"Nome: {nome} \nIdade: {idade} \nAltura: {altura}")

if idade >= 18:
    print('Você pode dirigir!')
else:
    print('Você ainda não pode dirigir!')
