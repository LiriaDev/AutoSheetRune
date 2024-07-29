import customtkinter as ctk
import json
import utils.funcoes.roll_dice as roll
from utils.alterar_status import criar_janela_vida, criar_janela_sani
from functools import partial
from utils.level_up import open_level_up

body: int
soul: int
appea: int
intele: int

character = 'char'


class Select(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry('400x300')
        self.title('Escolher Personagem')
        global name
        name = ctk.CTkEntry(self, height=10)
        button = ctk.CTkButton(self, text='Verificar e abrir', command=verify)
        name.grid(column=0, row=0, padx=10, pady=10)
        button.grid(column=0, row=1, padx=10, pady=10)


def verify():
    global nome
    nome = str(name.get())
    with open(f'{nome}.json', 'r') as f:
        global data
        data = json.load(f)
    if data != None:
        body = int(data['Corpo'])
        soul = int(data['Alma'])
        appea = int(data['Aparencia'])
        intele = int(data['Intelecto'])
        win = Manage()
        win_verify.destroy()


class Manage(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title(f'{data['Nome']}')
        self.geometry('700x600')
        body_rolar = ctk.CTkButton(self, text='Corpo', command=rolar_corpo)
        soul_rolar = ctk.CTkButton(self, text='Alma', command=rolar_alma)
        appea_rolar = ctk.CTkButton(self, text='Aparencia', command=rolar_aparencia)
        intele_rolar = ctk.CTkButton(self, text='Intelecto', command=rolar_intelecto)

        global result_label
        global success_fail
        result_label = ctk.CTkLabel(self, text='0', text_color='black', font=ctk.CTkFont(family='Arial', size=30))
        success_fail = ctk.CTkLabel(self, text=' ', font=ctk.CTkFont(family='Arial', size=30))

        name_label = ctk.CTkLabel(self, text=f'Nome: {data['Nome']}', font=ctk.CTkFont(family='Arial', size=20))
        race_label = ctk.CTkLabel(self, text=f'Raça: {data['raca']}', font=ctk.CTkFont(family='Arial', size=20))
        gender_label = ctk.CTkLabel(self, text=f'Gênero: {data['Genero']}', font=ctk.CTkFont(family='Arial', size=20))
        occu_label = ctk.CTkLabel(self, text=f'Ocupação: {data['Ocupacao']}', font=ctk.CTkFont(family='Arial', size=20))

        name_label.grid(column=0, row=5, padx=10, pady=10)
        race_label.grid(column=0, row=6, padx=10, pady=10)
        gender_label.grid(column=0, row=7, padx=10, pady=10)
        occu_label.grid(column=0, row=8, padx=10, pady=10)

        global vita_label
        global sani_label
        vita_label = ctk.CTkLabel(self, text=f'Vitalidade: {data['Vitalidade_Atual']}/{data['Vitalidade_Total']}',
                                  font=ctk.CTkFont(family='Arial', size=20))
        sani_label = ctk.CTkLabel(self, text=f'Sanidade: {data['Sanidade_Atual']}/{data['Sanidade_Total']}',
                                  font=ctk.CTkFont(family='Arial', size=20))

        vita_label.grid(column=2, row=5, padx=10, pady=10)
        sani_label.grid(column=2, row=6, padx=10, pady=10)
        vita_alterar = ctk.CTkButton(self, text='Alterar', command=partial(criar_janela_vida, data))
        sani_alterar = ctk.CTkButton(self, text='Alterar', command=partial(criar_janela_sani, data))
        vita_alterar.grid(column=3, row=5, padx=10, pady=10)
        sani_alterar.grid(column=3, row=6, padx=10, pady=10)

        level_up = ctk.CTkButton(self, text='Level up!', command=partial(open_level_up, data))
        level_up.grid(column=2, row=7, padx=10, pady=10)

        body_rolar.grid(column=0, row=1, padx=10, pady=10)
        soul_rolar.grid(column=0, row=2, padx=10, pady=10)
        appea_rolar.grid(column=0, row=3, padx=10, pady=10)
        intele_rolar.grid(column=0, row=4, padx=10, pady=10)
        result_label.grid(column=1, row=2, padx=10, pady=10)
        success_fail.grid(column=1, row=3, padx=10, pady=10)


def criar_janela():
    global win_verify
    win_verify = Select()


def rolar_corpo():
    result = roll.teste_rolagem()
    status = int(data['Corpo'])
    if result <= status:
        result_label.configure(text=str(result), text_color='green')
        success_fail.configure(text='Sucesso!', text_color='green')
    else:
        result_label.configure(text=str(result), text_color='red')
        success_fail.configure(text='Falha', text_color='red')


def rolar_alma():
    result = roll.teste_rolagem()
    status = int(data['Alma'])
    if result <= status:
        result_label.configure(text=str(result), text_color='green')
        success_fail.configure(text='Sucesso', text_color='green')


    else:
        result_label.configure(text=str(result), text_color='red')
        success_fail.configure(text='Falha', text_color='red')


def rolar_aparencia():
    result = roll.teste_rolagem()
    status = int(data['Aparencia'])
    if result <= status:
        result_label.configure(text=str(result), text_color='green')
        success_fail.configure(text='Sucesso', text_color='green')


    else:
        result_label.configure(text=str(result), text_color='red')
        success_fail.configure(text='Falha', text_color='red')


def rolar_intelecto():
    result = roll.teste_rolagem()
    status = int(data['Intelecto'])
    if result <= status:
        result_label.configure(text=str(result), text_color='green')
        success_fail.configure(text='Sucesso', text_color='green')


    else:
        result_label.configure(text=str(result), text_color='red')
        success_fail.configure(text='Falha', text_color='red')

def update_vita():
    vita = int(((int(data['Corpo']) + int(data['Aparencia'])) - 50) / 10 * 5 + 10)
    arquivo = open(f'{data['Nome']}.json', 'r+')
    data['Vitalidade_Total'] = vita
    json.dump(data, arquivo)
    vita_label.configure(text=f'Vitalidade: {data['Vitalidade_Atual']}/{data['Vitalidade_Total']}')

def update_sani():
    sani = int(((int(data['Alma']) + int(data['Intelecto'])) - 50) / 10 * 5 + 10)
    arquivo = open(f'{data['Nome']}.json', 'r+')
    data['Sanidade_Total'] = sani
    json.dump(data, arquivo)
    sani_label.configure(text=f'Sanidade: {data['Sanidade_Atual']}/{data['Sanidade_Total']}')