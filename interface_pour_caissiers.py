from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
from interface_pour_affichage_stocks import affichage_de_stocks
from interface_pour_ticket_caisse import ticket_caisse
from interface_pour_export_statique import export_statique

def interface_caissiers():
    interface_pour_le_caissiers = Tk()
    interface_pour_le_caissiers.title(string = "GesMag")
    interface_pour_le_caissiers.configure(bg = '#FFFFFF')

    x = 693
    y = 255

    fenetre_largeur = interface_pour_le_caissiers.winfo_screenwidth()
    fenetre_hauteur = interface_pour_le_caissiers.winfo_screenheight()

    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)

    interface_pour_le_caissiers.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')


    label_veuillez_choisir = Label(interface_pour_le_caissiers, text = "Caissier", font = ("Arial", 15, 'bold'), fg = 'white', bg = '#375D81', width = 13, height = 1, bd = 3, relief = 'groove')
    label_veuillez_choisir.grid(row = 0, columnspan = 2, pady = 10)


    ajouter_un_nouveau_cassier = Radiobutton(interface_pour_le_caissiers, text = "Afficher les stocks", font = ('Arial', 12, 'bold'), value = 1, indicatoron = 0, width = 30, height = 2, bg = 'white', fg = 'black', activebackground = '#e3e3e3', activeforeground = 'black', cursor = 'hand2', command = affichage_de_stocks)
    ajouter_un_nouveau_cassier.grid(row = 1, column = 0, padx = 35, pady = 10)


    ajouter_un_nouveau_cassier = Radiobutton(interface_pour_le_caissiers, text = "Ticket de caisse", font = ('Arial', 12, 'bold'), value = 2, indicatoron = 0, width = 30, height = 2, bg = 'white', fg = 'black', activebackground = '#e3e3e3', activeforeground = 'black', cursor = 'hand2', command = ticket_caisse)
    ajouter_un_nouveau_cassier.grid(row = 1, column = 1, padx = 35, pady = 10)


    afficher_des_caissiers = Radiobutton(interface_pour_le_caissiers, text = "Export statique", font = ('Arial', 12, 'bold'), value = 3, indicatoron = 0, width = 30, height = 2, bg = 'white', fg = 'black', activebackground = '#e3e3e3', activeforeground = 'black', cursor = 'hand2', command = export_statique)
    afficher_des_caissiers.grid(row = 2, columnspan = 2, padx = 35, pady = 10)


    def quitter():
        interface_pour_le_caissiers.destroy()


    bouton_pour_quitter = Button(interface_pour_le_caissiers, text = "Quitter", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#F32665', activebackground = '#F32665', activeforeground = 'white', cursor = 'hand2', command = quitter)
    bouton_pour_quitter.grid(row = 4, columnspan = 2, pady = 30)


    #interface_pour_le_caissiers.mainloop()
