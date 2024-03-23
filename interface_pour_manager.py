from tkinter import *
from interface_pour_ajout_de_managers import interface_ajout_managers
from interface_pour_ajout_de_caissiers import interface_ajout_caissiers
from interface_pour_affichage_de_caissiers_et_managers import interface_affichage_caissiers_managers
from interface_pour_suppression_de_caissiers import interface_suppression_caissiers_managers
from interface_pour_caissiers import interface_caissiers
from interface_pour_suivi_de_vente import interface_suivi_de_vente


def interface_manager():
    interface_pour_le_manager = Tk()
    interface_pour_le_manager.title(string = "GesMag")
    interface_pour_le_manager.configure(bg = '#FFFFFF')

    x = 693
    y = 322

    fenetre_largeur = interface_pour_le_manager.winfo_screenwidth()
    fenetre_hauteur = interface_pour_le_manager.winfo_screenheight()

    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)

    interface_pour_le_manager.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')


    label_veuillez_choisir = Label(interface_pour_le_manager, text = "Manager", font = ("Arial", 15, 'bold'), fg = 'white', bg = '#375D81', width = 13, height = 1, bd = 3, relief = 'groove')
    label_veuillez_choisir.grid(row = 0, columnspan = 2, pady = 10)


    ajouter_un_nouveau_cassier = Radiobutton(interface_pour_le_manager, text = "Ajouter un manager", font = ('Arial', 12, 'bold'), value = 1, indicatoron = 0, width = 30, height = 2, bg = 'white', fg = 'black', activebackground = '#e3e3e3', activeforeground = 'black', cursor = 'hand2', command = interface_ajout_managers)
    ajouter_un_nouveau_cassier.grid(row = 1, column = 0, padx = 35, pady = 10)


    ajouter_un_nouveau_cassier = Radiobutton(interface_pour_le_manager, text = "Ajouter un caisier", font = ('Arial', 12, 'bold'), value = 2, indicatoron = 0, width = 30, height = 2, bg = 'white', fg = 'black', activebackground = '#e3e3e3', activeforeground = 'black', cursor = 'hand2', command = interface_ajout_caissiers)
    ajouter_un_nouveau_cassier.grid(row = 1, column = 1, padx = 35, pady = 10)


    afficher_des_caissiers = Radiobutton(interface_pour_le_manager, text = "Afficher les managers / cassiers", font = ('Arial', 12, 'bold'), value = 3, indicatoron = 0, width = 30, height = 2, bg = 'white', fg = 'black', activebackground = '#e3e3e3', activeforeground = 'black', cursor = 'hand2', command = interface_affichage_caissiers_managers)
    afficher_des_caissiers.grid(row = 2, column = 0, padx = 35, pady = 10)


    supprimer_un_caissier = Radiobutton(interface_pour_le_manager, text = "Supprimer un manager / caissier", font = ('Arial', 12, 'bold'), value = 4, indicatoron = 0, width = 30, height = 2, bg = 'white', fg = 'black', activebackground = '#e3e3e3', activeforeground = 'black', cursor = 'hand2', command = interface_suppression_caissiers_managers)
    supprimer_un_caissier.grid(row = 2, column = 1, padx = 35, pady = 10)


    suivre_de_vente = Radiobutton(interface_pour_le_manager, text = "Suivi de vente", font = ('Arial', 12, 'bold'), value = 5, indicatoron = 0, width = 30, height = 2, bg = 'white', fg = 'black', activebackground = '#e3e3e3', activeforeground = 'black', cursor = 'hand2', command = interface_suivi_de_vente)
    suivre_de_vente.grid(row = 3, column = 0, padx = 35, pady = 10)


    interface_de_caissiers = Radiobutton(interface_pour_le_manager, text = "Caissiers", font = ('Arial', 12, 'bold'), value = 6, indicatoron = 0, width = 30, height = 2, bg = 'white', fg = 'black', activebackground = '#e3e3e3', activeforeground = 'black', cursor = 'hand2', command = interface_caissiers)
    interface_de_caissiers.grid(row = 3, column = 1, padx = 35, pady = 10)


    def quitter():
        interface_pour_le_manager.destroy()


    bouton_pour_quitter = Button(interface_pour_le_manager, text = "Quitter", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#F32665', activebackground = '#F32665', activeforeground = 'white', cursor = 'hand2', command = quitter)
    bouton_pour_quitter.grid(row = 4, columnspan = 2, pady = 30)

    


#interface_pour_le_manager.mainloop()