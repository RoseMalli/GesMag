from tkinter import *
import pandas as pd
from tkinter import ttk

def export_statique():
    interface_pour_export_statique = Tk()
    interface_pour_export_statique.title(string = "GesMag")
    interface_pour_export_statique.configure(bg = 'white')

    x = 417
    y = 370

    fenetre_largeur = interface_pour_export_statique.winfo_screenwidth()
    fenetre_hauteur = interface_pour_export_statique.winfo_screenheight()

    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)

    interface_pour_export_statique.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_stocker_montant_total = Label(interface_pour_export_statique, text = "Stockage du montant total", font = ("Arial", 15, 'bold'), fg = 'white', bg = '#375D81', width = 28, height = 1, bd = 3, relief = 'groove')
    label_stocker_montant_total.grid(row = 0, columnspan = 2, pady = 10)


    style = ttk.Style()
    style.theme_use('clam')
    style.configure('Treeview', rowheight = 25)
    style.map('Treeview', background = [('selected', '#74BBE4')])


    tableau = ttk.Treeview(interface_pour_export_statique, selectmode = 'browse')
    tableau.grid(row = 1, column = 0, pady = 10)

    scrollbar = ttk.Scrollbar(interface_pour_export_statique, orient = 'vertical', command = tableau.yview)
    scrollbar.grid(row = 1, column = 1, sticky = NS, pady = 10)

    tableau.configure(yscrollcommand = scrollbar.set)

    def quitter():
            interface_pour_export_statique.destroy()

    bouton_pour_quitter = Button(interface_pour_export_statique, text = "Quitter", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#F32665', activebackground = '#F32665', activeforeground = 'white', cursor = 'hand2', command = quitter)
    bouton_pour_quitter.grid(pady = 30)


    data = pd.read_excel('ticket_de_caisse.xlsx')

    tableau["column"] = list(data.columns)
    tableau["show"] = "headings"
    for colonne in tableau["column"]:
        tableau.heading(colonne, text = colonne)


    data_ligne = data.to_numpy().tolist()
    for ligne in data_ligne:
        tableau.insert("", "end", values = ligne)


    #interface_pour_export_statique.mainloop()