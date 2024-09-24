CEP= [110,220,330,440,550,660,770,880,990]
msg= '13059- '
 
#Aqui há duas variáveis pois em cada uma armazemanos um dados sobre a lista; 'lista' armazena a posição do valor na lista, enquanto 'indice' armazena o valor de cada item na lista.
for lista, indice in enumerate(CEP):
    #Aqui temos a msg (13059-) que é imutável até o momento; temos + para concatenar os dois valores indicados no print; e temos indice que traz o valor do intem na lista.
    print(msg + format(indice))