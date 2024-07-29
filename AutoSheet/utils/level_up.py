import customtkinter as ctk
import json
from functools import partial

global levels
levels = 0

class LevelUpWindow(ctk.CTkToplevel):
    def __init__(self, data):
        super().__init__()

        body_up = ctk.CTkButton(self, text='Aumentar', command=up_level)
        soul_up = ctk.CTkButton(self, text='Diminuir', command=remove_level)
        confirm = ctk.CTkButton(self, text='Confirmar', command=partial(confirm_choice, data))
        cancel = ctk.CTkButton(self, text='Cancelar', command=close_window)

        global choice
        choice = ctk.CTkOptionMenu(self, values=['Corpo', 'Alma', 'Aparencia', 'Intelecto'])

        global label
        label = ctk.CTkLabel(self, text=' ', font=ctk.CTkFont(family='Arial', size=20))

        body_up.grid(column=0, row=1, padx=10, pady=10)
        soul_up.grid(column=0, row=2, padx=10, pady=10)

        label.grid(column=1, row=2, padx=10, pady=10)
        choice.grid(column=1, row=1, padx=10, pady=10)
        confirm.grid(column=1, row=3, padx=10, pady=10)
        cancel.grid(column=1, row=4, padx=10, pady=10)


def open_level_up(data):
    global win
    win = LevelUpWindow(data)


def add_quant():
    global levels
    levels = levels + 5

def remove_quant():
    global levels
    levels = levels - 5


def up_level():
    add_level = add_quant()
    label.configure(text=f'{choice.get()} + {levels}')



def remove_level():
    remove_quant()
    label.configure(text=f'{choice.get()} + {levels}')


def confirm_choice(data):
    from utils.manage import update_sani, update_vita

    arquivo = open(f'{data['Nome']}.json', 'r+')
    data[choice.get()] = data[choice.get()] + levels
    json.dump(data, arquivo)
    update_sani()
    update_vita()
    close_window()


def close_window():
    global levels
    levels = 0
    win.destroy()
