from tkinter import *
import pandas as pd
from interface_pour_manager import interface_manager
from interface_pour_caissiers import interface_caissiers
from messages import *


interface_de_connexion = Tk()
interface_de_connexion.title(string = "GesMag")
interface_de_connexion.configure(bg = '#FFFFFF')


x = 452
y = 230


fenetre_largeur = interface_de_connexion.winfo_screenwidth()
fenetre_hauteur = interface_de_connexion.winfo_screenheight()


largeur = (fenetre_largeur / 2) - (x / 2)
hauteur = (fenetre_hauteur / 2) - (y /2)


interface_de_connexion.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')


label_connectez_vous = Label(interface_de_connexion, text = "Login", font = ("Arial", 15, 'bold'), fg = 'white', bg = '#375D81', width = 10, height = 1, bd = 3, relief = 'groove')
label_connectez_vous.grid(row = 0, columnspan = 2, pady = 10)


label_pour_indentifiant = Label(interface_de_connexion, text = "Identifiant :", font = ("Arial", 12, 'bold'), bg = 'white')
label_pour_indentifiant.grid(row = 1, column = 0, sticky = W, padx = 35, pady = 10)
zone_de_saisi_pour_identifiant = Entry(interface_de_connexion, font = ("Arial", 12), bg = '#e3e3e3',width = 20, bd = 3)
zone_de_saisi_pour_identifiant.grid(row = 1, column = 1, sticky = E, padx = 35, pady = 10)
zone_de_saisi_pour_identifiant.focus()


label_pour_le_mot_de_passe = Label(interface_de_connexion, text = "Mot de passe :", font = ("Arial", 12, 'bold'), bg = 'white')
label_pour_le_mot_de_passe.grid(row = 2, column = 0, sticky = W, padx = 35, pady = 10)
zone_de_saisi_pour_mot_de_passe = Entry(interface_de_connexion, font = ("Arial", 12), bg = '#e3e3e3', width = 20, bd = 3, show = '*')
zone_de_saisi_pour_mot_de_passe.grid(row = 2, column = 1, sticky = E, padx = 35, pady = 10)


data = pd.read_excel('base_de_données_caissiers_et_managers.xlsx')


def verification_de_connexion():
    if len(zone_de_saisi_pour_identifiant.get()) == 0 and len(zone_de_saisi_pour_mot_de_passe.get()) == 0:
        connectez_vous()
    mask = data["Identifiant"].values
    if zone_de_saisi_pour_identifiant.get() in mask:
        if zone_de_saisi_pour_identifiant.get().startswith('C'):
            mask2 = data.loc[data["Identifiant"] == zone_de_saisi_pour_identifiant.get(), "Mot de passe"].values[0]
            if zone_de_saisi_pour_mot_de_passe.get() == mask2:
                interface_caissiers()
                zone_de_saisi_pour_identifiant.delete(0, END)
                zone_de_saisi_pour_mot_de_passe.delete(0, END)
                zone_de_saisi_pour_identifiant.focus()
            else:
                zone_de_saisi_pour_mot_de_passe.delete(0, END)
                mot_de_passe_incorrect()
                zone_de_saisi_pour_mot_de_passe.focus()
        elif zone_de_saisi_pour_identifiant.get().startswith('M'):
            mask2 = data.loc[data["Identifiant"] == zone_de_saisi_pour_identifiant.get(), "Mot de passe"].values[0]
            if zone_de_saisi_pour_mot_de_passe.get() == mask2:
                interface_manager()
                zone_de_saisi_pour_identifiant.delete(0, END)
                zone_de_saisi_pour_mot_de_passe.delete(0, END)
                zone_de_saisi_pour_identifiant.focus()
            else: 
                zone_de_saisi_pour_mot_de_passe.delete(0, END)
                zone_de_saisi_pour_mot_de_passe.focus()
                mot_de_passe_incorrect()
    else:
        zone_de_saisi_pour_identifiant.delete(0, END)
        zone_de_saisi_pour_mot_de_passe.delete(0, END)
        zone_de_saisi_pour_identifiant.focus()
        identifiant_incorrect()
       

bouton_pour_connexion = Button(interface_de_connexion, text = "Connexion", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#6FC771', activebackground = '#6FC771', activeforeground = 'white', cursor = 'hand2', command = verification_de_connexion)
bouton_pour_connexion.grid(row = 3, column = 1, sticky = E, padx = 35, pady = 30)


bouton_pour_quitter = Button(interface_de_connexion, text = "Quitter", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#F32665', activebackground = '#F32665', activeforeground = 'white', cursor = 'hand2', command = quit)
bouton_pour_quitter.grid(row = 3, column = 0, sticky = W, padx = 35, pady = 30)


interface_de_connexion.mainloop()