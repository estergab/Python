#Importa a biblioteca Tkinter
import tkinter as tk

#Função que vai substituir a label
def hlw():
    label.config(text = 'Hello World!')

#Cria janela
janela = tk.Tk()
#Título da janela
janela.title('Hello word app')
#Tamanho da janela
janela.geometry('250x100')

#Criar label
label= tk.Label(janela, text='')
#Exibe a label
label.pack()

#Criar botão com texto 'Clique aqui', ele executa a função criada
botao = tk.Button(janela, text='Clique aqui', command=hlw)
#Mostrar botão
botao.pack()

#Mantem a janela aberta
janela.mainloop()