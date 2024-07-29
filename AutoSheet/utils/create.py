import customtkinter as ctk
import json


def registrar_personagem():
    name_final = str(name_box.get())
    race_final = str(race_box.get())
    gender_final = str(gender_box.get())
    occup_final = str(occupation_box.get())
    body_final = str(body_box.get())
    soul_final = str(soul_box.get())
    appea_final = str(appearence_box.get())
    intele_final = str(intelect_box.get())

    vita = int(((int(body_final) + int(appea_final)) - 50) / 10 * 5 + 10)
    sani = int((int(soul_final) + int(intele_final) - 50) / 10 * 5 + 10)

    character = {
        "Nome": name_final,
        'raca': race_final,
        'Genero': gender_final,
        'Ocupacao':occup_final,
        'Corpo': body_final,
        'Alma': soul_final,
        'Aparencia': appea_final,
        'Intelecto': intele_final,
        'Sincronia': '50',
        'Vitalidade_Atual': vita,
        'Vitalidade_Total': vita,
        'Sanidade_Atual': sani,
        'Sanidade_Total': sani

    }
    with open(f'{name_final}.json', 'w') as arquivo:
        json.dump(character, arquivo)
    close_window()

def close_window():
    win.destroy()


class Window(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        name_label = ctk.CTkLabel(self, text='Nome:')
        race_label = ctk.CTkLabel(self, text='Raça:')
        gender_label = ctk.CTkLabel(self, text='Gênero:')
        occupation_label = ctk.CTkLabel(self, text='Ocupação:')
        name_label.grid(column=0, row=1, padx=10,pady=10)
        race_label.grid(column=0, row=2, padx=10,pady=10)
        gender_label.grid(column=0, row=3, padx=10,pady=10)
        occupation_label.grid(column=0, row=4, padx=10,pady=10)

        global name_box
        global race_box
        global gender_box
        global occupation_box
        global body_box
        global soul_box
        global appearence_box
        global intelect_box

        name_box = ctk.CTkEntry(self, height=10)
        race_box = ctk.CTkEntry(self, height=10)
        gender_box = ctk.CTkEntry(self, height=10)
        occupation_box = ctk.CTkEntry(self, height=10)
        name_box.grid(column=1, row=1, padx=10, pady=10)
        race_box.grid(column=1, row=2, padx=10, pady=10)
        gender_box.grid(column=1, row=3, padx=10, pady=10)
        occupation_box.grid(column=1, row=4, padx=10, pady=10)

        body_label = ctk.CTkLabel(self, text='Corpo:')
        soul_label = ctk.CTkLabel(self, text='Alma:')
        appearence_label = ctk.CTkLabel(self, text='Aparência')
        intelect_label = ctk.CTkLabel(self, text='Intelecto')
        body_label.grid(column=2, row=1, padx=10, pady=10)
        soul_label.grid(column=2, row=2, padx=10, pady=10)
        appearence_label.grid(column=2, row=3, padx=10, pady=10)
        intelect_label.grid(column=2, row=4, padx=10, pady=10)

        body_box = ctk.CTkEntry(self, height=10)
        soul_box = ctk.CTkEntry(self, height=10)
        appearence_box = ctk.CTkEntry(self, height=10)
        intelect_box = ctk.CTkEntry(self, height=10)
        body_box.grid(column=3, row=1, padx=10, pady=10)
        soul_box.grid(column=3, row=2, padx=10, pady=10)
        appearence_box.grid(column=3, row=3, padx=10, pady=10)
        intelect_box.grid(column=3, row=4, padx=10, pady=10)

        reg = registrar_personagem
        botao_criar = ctk.CTkButton(self, text='Finalizar', command=registrar_personagem)
        botao_criar.grid(column=4, row=3)
        self.title('Criar Personagem')
        self.geometry('700x300')




def create_window():
    global win
    win = Window()











