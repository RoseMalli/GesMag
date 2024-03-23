from tkinter import *
import pandas as pd
from tkinter import ttk
from messages import identifiant_incorrect

def interface_affichage_caissiers_managers():
    interface_pour_afficher_les_caissiers_et_les_managers = Toplevel()
    interface_pour_afficher_les_caissiers_et_les_managers.title(string = "GesMag")
    interface_pour_afficher_les_caissiers_et_les_managers.configure(bg = 'white')


    x = 1620
    y = 490


    fenetre_largeur = interface_pour_afficher_les_caissiers_et_les_managers.winfo_screenwidth()
    fenetre_hauteur = interface_pour_afficher_les_caissiers_et_les_managers.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_afficher_les_caissiers_et_les_managers.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')


    label_afficher_caissier = Label(interface_pour_afficher_les_caissiers_et_les_managers, text = "Affichage des caissiers / managers", font = ("Arial", 15, 'bold'), fg = 'white', bg = '#375D81', width = 35, height = 1, bd = 3, relief = 'groove')
    label_afficher_caissier.grid(row = 0, columnspan = 2, pady = 10)


    frame = Frame(interface_pour_afficher_les_caissiers_et_les_managers, width = 865, height = 120, bg = 'white')
    frame.grid(row = 1, pady = 10)
    frame.grid_propagate(0)


    label_trouver_identifiant_caissier = Label(frame, text = "Identifiant :", font = ("Arial", 12, 'bold'), bg = 'white')
    label_trouver_identifiant_caissier.grid(row = 0, column = 0, padx = 35, pady = 10)
    zone_de_saisi_trouver_identifiant_caissier = Entry(frame, font = ("Arial", 12), bg = '#e3e3e3', bd = 3, width = 27)
    zone_de_saisi_trouver_identifiant_caissier.grid(row = 0, column = 1, padx = 35, pady = 10)
    zone_de_saisi_trouver_identifiant_caissier.focus()


    tableau = ttk.Treeview(interface_pour_afficher_les_caissiers_et_les_managers)
    tableau.grid(row = 2, column = 0)

    scrollbar = ttk.Scrollbar(interface_pour_afficher_les_caissiers_et_les_managers, orient = 'vertical', command = tableau.yview)
    scrollbar.grid(row = 2, column = 1, sticky = NS)

    tableau.configure(yscrollcommand = scrollbar.set)


    data = pd.read_excel('base_de_données_caissiers_et_managers.xlsx')


    tableau["column"] = list(data.columns)
    tableau["show"] = "headings"
    for colonne in tableau["column"]:
        tableau.heading(colonne, text = colonne)


    def afficher():
        une_seule_fois()
        trouver = data["Identifiant"].values
        if zone_de_saisi_trouver_identifiant_caissier.get() in trouver:
            data1 = pd.read_excel('base_de_données_caissiers_et_managers.xlsx', index_col = "Identifiant")
            searched = data1.loc[zone_de_saisi_trouver_identifiant_caissier.get()]
            tableau.insert("","end", values = (zone_de_saisi_trouver_identifiant_caissier.get() + " " + str(searched.values.tolist())[1:-1]))
        else:
            zone_de_saisi_trouver_identifiant_caissier.delete(0, END)
            zone_de_saisi_trouver_identifiant_caissier.focus()
            identifiant_incorrect()


    def afficher_tous():
        une_seule_fois()
        data_ligne = data.to_numpy().tolist()
        for ligne in data_ligne:
            tableau.insert("", "end", values = ligne)
            


    def une_seule_fois():
        tableau.delete(*tableau.get_children())


    def vider():
        zone_de_saisi_trouver_identifiant_caissier.delete(0, END)


    def quitter():
        interface_pour_afficher_les_caissiers_et_les_managers.destroy()


    bouton_pour_afficher = Button(frame, text = "Afficher", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#6FC771', activebackground = '#6FC771', activeforeground = 'white', cursor = 'hand2', command = afficher)
    bouton_pour_afficher.grid(row = 0, column = 3, padx = 35, pady = 10, sticky = E)


    bouton_pour_afficher_tous = Button(frame, text = "Afficher tous", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#6FC771', activebackground = '#6FC771', activeforeground = 'white', cursor = 'hand2', command = afficher_tous)
    bouton_pour_afficher_tous.grid(row = 2, column = 3, padx = 35, pady = 10, sticky = E)


    bouton_pour_vider = Button(frame, text = "Vider", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#F4D03F', activebackground = '#F4D03F', activeforeground = 'white', cursor = 'hand2', command = vider)
    bouton_pour_vider.grid(row = 0, column = 4, padx = 35, pady = 10, sticky = E)


    bouton_pour_quitter = Button(interface_pour_afficher_les_caissiers_et_les_managers, text = "Quitter", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#F32665', activebackground = '#F32665', activeforeground = 'white', cursor = 'hand2', command = quitter)
    bouton_pour_quitter.grid(pady = 30)


#interface_pour_afficher_les_caissiers_et_les_managers.mainloop()