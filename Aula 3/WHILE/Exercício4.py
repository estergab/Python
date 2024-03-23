ContVoltas= 1
NumInt = 0

while ContVoltas < 6:
    x= int(input(f'Digite {ContVoltas}º número inteiro: '))
    NumInt= NumInt + x
    ContVoltas = ContVoltas + 1
    
    
Media= NumInt/5
print(f'A média é {Media}')

