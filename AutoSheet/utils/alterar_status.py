import json
import customtkinter as ctk
import utils.funcoes.data_reader as read
from functools import partial

class Sani_alterar(ctk.CTkToplevel):
    def __init__(self, data):
        super().__init__()

        label1 = ctk.CTkLabel(self, text='Alterar Sanidade: ')
        global sani
        sani = ctk.CTkEntry(self, height=10, placeholder_text=data['Sanidade_Atual'])
        diminuir_vida = ctk.CTkButton(self, text='-', command=partial(dano_sani, data))
        aumentar_vida = ctk.CTkButton(self, text='+', command=partial(curar_sani, data))
        global error_label_sani
        error_label_sani = ctk.CTkLabel(self, text=' ')
        label1.grid(column=0, row=0, padx=10, pady=10)
        diminuir_vida.grid(column=0, row=1, padx=10, pady=10)
        sani.grid(column=1, row=1, padx=10, pady=10)
        aumentar_vida.grid(column=2, row=1, padx=10, pady=10)


class Vida_alterar(ctk.CTkToplevel):
    def __init__(self, data):
        super().__init__()

        label1 = ctk.CTkLabel(self, text='Alterar Vida: ')
        global life
        life = ctk.CTkEntry(self, height=10, placeholder_text=data['Vitalidade_Atual'])
        diminuir_vida = ctk.CTkButton(self, text='-', command=partial(dano_vita, data))
        aumentar_vida = ctk.CTkButton(self, text='+', command=partial(curar_vita, data))
        global error_label
        error_label = ctk.CTkLabel(self, text=' ')
        label1.grid(column=0, row=0, padx=10, pady=10)
        diminuir_vida.grid(column=0, row=1, padx=10, pady=10)
        life.grid(column=1, row=1, padx=10, pady=10)
        aumentar_vida.grid(column=2, row=1, padx=10, pady=10)


def criar_janela_vida(data):
    win = Vida_alterar(data)

def criar_janela_sani(data):
    win = Sani_alterar(data)

def curar_vita(data):
    from utils.manage import update_vita

    if data['Vitalidade_Atual'] >= data['Vitalidade_Total']:
        error_label.configure(text='Vida Maxima Atingida')
    else:
        vida = int(data['Vitalidade_Atual'] + 1)
        arquivo = open(f'{data['Nome']}.json', 'r+')
        data['Vitalidade_Atual'] = vida
        json.dump(data, arquivo)
        life.delete(0, 'end')
        life.insert(string=str(data['Vitalidade_Atual']), index=1)
        update_vita()


def dano_vita(data):
    from utils.manage import update_vita

    if data['Vitalidade_Atual'] <= 0:
        error_label.configure(text='Vida não pode ir abaixo de 0')
    else:
        vida = int(data["Vitalidade_Atual"] - 1)
        arquivo = open(f'{data['Nome']}.json', 'r+')
        data['Vitalidade_Atual'] = vida
        json.dump(data, arquivo)
        life.delete(0, 'end')
        life.insert(string=str(data['Vitalidade_Atual']), index=1)
        update_vita()

def dano_sani(data):
    from utils.manage import update_sani

    if data['Sanidade_Atual'] <= 0:
        error_label.configure(text='Sanidade não pode ir abaixo de 0')
    else:
        vida = int(data["Sanidade_Atual"] - 1)
        arquivo = open(f'{data['Nome']}.json', 'r+')
        data['Sanidade_Atual'] = vida
        json.dump(data, arquivo)
        sani.delete(0, 'end')
        sani.configure(placeholder_text=data['Sanidade_Atual'])
        update_sani()

def curar_sani(data):
    from utils.manage import update_sani

    if data['Sanidade_Atual'] >= data['Sanidade_Total']:
        error_label.configure(text='Sanidade maxima atingida')
    else:
        vida = int(data["Sanidade_Atual"] + 1)
        arquivo = open(f'{data['Nome']}.json', 'r+')
        data['Sanidade_Atual'] = vida
        json.dump(data, arquivo)
        sani.delete(0, 'end')
        sani.configure(placeholder_text=data['Sanidade_Atual'])

        update_sani()