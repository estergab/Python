
#1 Procurar um valor em uma lista: 

fruits =['ABACATE', 'UVA', 'STROGONOFF']
un= [10, 30, 1]
choice = input('Digite o nome da fruta para verificarmos se há disponível em estoque: ').upper().strip()

if choice in fruits:
    id= fruits.index(choice)
    un_id = un[id]
    print(f'A fruta {choice} possui {un_id} unidade(s) disponível(s) em estoque!')
else:
    print(f'Não temos {choice} disponível em estoque!')



#2 Adicionar mais itens em uma lista: .append() 
produtos= ['MEXIRICA', 'ÁGUA', 'DIESEL']
novoitem= input('Digite o nome do produto a ser adicionado: ').upper().strip()

if novoitem in produtos:
    print(f'Já existe um produto com o nome{novoitem}')
else:
    produtos.append(novoitem)
    print(f'Produto "{novoitem}" adicionado à lista com sucesso!')
    print(produtos)





#3 Remover intem da lista: .remove()
produtos= ['ABACATE', 'UVA', 'STROGONOFF']
delitem= input('Digite o nome do produto a ser removido: ').upper().strip()

if delitem in produtos:
    produtos.remove(delitem)
    print('Produto removido do estoque com sucesso!')
    print(produtos)
else:
    print(f'Não temos {delitem} no estoque!')

