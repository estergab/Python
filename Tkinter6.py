import tkinter as tk

window = tk.Tk()

def diminuir():
    valor = int(lbl_valor['text'])
    lbl_valor['text'] = f'{valor - 1}'

def aumentar():
    valor = int(lbl_valor['text'])
    lbl_valor['text'] = f'{valor + 1}'

window.title('Contador')
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)  # Corrigido aqui

# btn = Button 
btn_diminuir = tk.Button(master=window, text='-', command=diminuir)  # Corrigido "test" para "text"
btn_diminuir.grid(row=0, column=0, sticky='nsew')

# lbl = Label
lbl_valor = tk.Label(master=window, text='0')
lbl_valor.grid(row=0, column=1)

btn_aumentar = tk.Button(master=window, text='+', command=aumentar)
btn_aumentar.grid(row=0, column=2, sticky='nsew')

window.mainloop()