num1 = float(input("Sou muito inteligente, quer ver? \nDigite um número: \n"))
num2 = float(input("Agora digite mais um: \n"))
num3 = float(input("O último agora, prometo: \n"))

maior = max(num1, num2, num3)

linha = '---------------------------'

print(f"{linha}\nO maior número é: {maior}\n{linha}")