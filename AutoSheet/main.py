import customtkinter as ctk
from utils.create import create_window
from utils.manage import criar_janela




win = ctk.CTk()
win.geometry('400x300')
win.title('AutoSheet Rune')

text = ctk.CTkLabel(win, text='Selecione a ação desejada')
text.pack()

botao_criar = ctk.CTkButton(win, text='Criar Personagem', command=create_window)
botao_criar.pack()

botao_gerenciar = ctk.CTkButton(win, text='Escolher Personagem', command=criar_janela).pack(padx=10,pady=10)

win.mainloop()






















