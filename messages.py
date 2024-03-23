from tkinter import *


def identifiant_incorrect():
    interface_pour_identifiant_incorrect = Tk()
    interface_pour_identifiant_incorrect.title(string = "GesMag")
    interface_pour_identifiant_incorrect.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_identifiant_incorrect.winfo_screenwidth()
    fenetre_hauteur = interface_pour_identifiant_incorrect.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_identifiant_incorrect.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_identifiant_incorrect = Label(interface_pour_identifiant_incorrect, text = "Erreur", font = ('Arial', 12, 'bold'), bg = '#FF0000', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_identifiant_incorrect.grid(row = 0, columnspan = 2, padx = 88, pady = 10)

    label_pour_message_erreur = Label(interface_pour_identifiant_incorrect, text = "Identifiant incorrect", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_erreur.grid(row = 1, columnspan = 2, padx = 88, pady = 10)

    bouton_pour_quitter = Button(interface_pour_identifiant_incorrect, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_identifiant_incorrect.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 88, pady = 10)

    interface_pour_identifiant_incorrect.mainloop()


def mot_de_passe_incorrect():
    interface_pour_mot_de_passe_incorrect = Tk()
    interface_pour_mot_de_passe_incorrect.title(string = "GesMag")
    interface_pour_mot_de_passe_incorrect.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_mot_de_passe_incorrect.winfo_screenwidth()
    fenetre_hauteur = interface_pour_mot_de_passe_incorrect.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_mot_de_passe_incorrect.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_mot_de_passe_incorrect = Label(interface_pour_mot_de_passe_incorrect, text = "Erreur", font = ('Arial', 12, 'bold'), bg = '#FF0000', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_mot_de_passe_incorrect.grid(row = 0, columnspan = 2, padx = 73, pady = 10)

    label_pour_message_erreur = Label(interface_pour_mot_de_passe_incorrect, text = "Mot de passe incorrect", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_erreur.grid(row = 1, columnspan = 2, padx = 73, pady = 10)

    bouton_pour_quitter = Button(interface_pour_mot_de_passe_incorrect, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_mot_de_passe_incorrect.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 73, pady = 10)

    interface_pour_mot_de_passe_incorrect.mainloop()


def saisissez_un_identifiant():
    interface_pour_saisissez_un_identifiant = Tk()
    interface_pour_saisissez_un_identifiant.title(string = "GesMag")
    interface_pour_saisissez_un_identifiant.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_saisissez_un_identifiant.winfo_screenwidth()
    fenetre_hauteur = interface_pour_saisissez_un_identifiant.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_saisissez_un_identifiant.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_saisissez_un_identifiant = Label(interface_pour_saisissez_un_identifiant, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_saisissez_un_identifiant.grid(row = 0, columnspan = 2, padx = 72, pady = 10)

    label_pour_message_alerte = Label(interface_pour_saisissez_un_identifiant, text = "Saisissez un identifiant", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 72, pady = 10)

    bouton_pour_quitter = Button(interface_pour_saisissez_un_identifiant, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_saisissez_un_identifiant.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 72, pady = 10)

    interface_pour_saisissez_un_identifiant.mainloop()


def pas_de_caracteres_speciaux():
    interface_pour_pas_de_caracteres_speciaux = Tk()
    interface_pour_pas_de_caracteres_speciaux.title(string = "GesMag")
    interface_pour_pas_de_caracteres_speciaux.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_pas_de_caracteres_speciaux.winfo_screenwidth()
    fenetre_hauteur = interface_pour_pas_de_caracteres_speciaux.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_pas_de_caracteres_speciaux.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_pas_de_caracteres_speciaux = Label(interface_pour_pas_de_caracteres_speciaux, text = "Erreur", font = ('Arial', 12, 'bold'), bg = '#FF0000', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_pas_de_caracteres_speciaux.grid(row = 0, columnspan = 2, padx = 57, pady = 10)

    label_pour_message_erreur = Label(interface_pour_pas_de_caracteres_speciaux, text = "Pas de caractères spéciaux", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_erreur.grid(row = 1, columnspan = 2, padx = 57, pady = 10)

    bouton_pour_quitter = Button(interface_pour_pas_de_caracteres_speciaux, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_pas_de_caracteres_speciaux.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 57, pady = 10)

    interface_pour_pas_de_caracteres_speciaux.mainloop()

def nom_en_majuscule():
    interface_pour_nom_en_masjucule = Tk()
    interface_pour_nom_en_masjucule.title(string = "GesMag")
    interface_pour_nom_en_masjucule.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_nom_en_majuscule.winfo_screenwidth()
    fenetre_hauteur = interface_pour_nom_en_majuscule.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_nom_en_majuscule.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_nom_en_masjucule = Label(interface_pour_nom_en_masjucule, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_nom_en_masjucule.grid(row = 0, columnspan = 2, padx = 15, pady = 10)

    label_pour_message_alerte = Label(interface_pour_nom_en_masjucule, text = "Ecrivez le nom en masjucule", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 15, pady = 10)

    bouton_pour_quitter = Button(interface_pour_nom_en_masjucule, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_nom_en_masjucule.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 15, pady = 10)

    interface_pour_nom_en_masjucule.mainloop()

def pas_de_minuscles():
    interface_pour_pas_de_minuscles = Tk()
    interface_pour_pas_de_minuscles.title(string = "GesMag")
    interface_pour_pas_de_minuscles.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_pas_de_minuscles.winfo_screenwidth()
    fenetre_hauteur = interface_pour_pas_de_minuscles.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_pas_de_minuscles.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_pas_de_minuscles = Label(interface_pour_pas_de_minuscles, text = "Erreur", font = ('Arial', 12, 'bold'), bg = '#FF0000', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_pas_de_minuscles.grid(row = 0, columnspan = 2, padx = 90, pady = 10)

    label_pour_message_erreur = Label(interface_pour_pas_de_minuscles, text = "Pas de minuscles", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_erreur.grid(row = 1, columnspan = 2, padx = 90, pady = 10)

    bouton_pour_quitter = Button(interface_pour_pas_de_minuscles, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_pas_de_minuscles.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 90, pady = 10)

    interface_pour_pas_de_minuscles.mainloop()

def identifiant_par_c():
    interface_pour_identifiant_par_c = Tk()
    interface_pour_identifiant_par_c.title(string = "GesMag")
    interface_pour_identifiant_par_c.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_identifiant_par_c.winfo_screenwidth()
    fenetre_hauteur = interface_pour_identifiant_par_c.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_identifiant_par_c.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_identifiant_par_c = Label(interface_pour_identifiant_par_c, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_identifiant_par_c.grid(row = 0, columnspan = 2, padx = 15, pady = 10)

    label_pour_message_alerte = Label(interface_pour_identifiant_par_c, text = "Identifiant devrait commencé par un 'C'", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 15, pady = 10)

    bouton_pour_quitter = Button(interface_pour_identifiant_par_c, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_identifiant_par_c.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 15, pady = 10)

    interface_pour_identifiant_par_c.mainloop()

def identifiant_par_m():
    interface_pour_identifiant_par_m = Tk()
    interface_pour_identifiant_par_m.title(string = "GesMag")
    interface_pour_identifiant_par_m.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_identifiant_par_m.winfo_screenwidth()
    fenetre_hauteur = interface_pour_identifiant_par_m.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_identifiant_par_m.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_identifiant_par_m = Label(interface_pour_identifiant_par_m, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_identifiant_par_m.grid(row = 0, columnspan = 2, padx = 15, pady = 10)

    label_pour_message_alerte = Label(interface_pour_identifiant_par_m, text = "Identifiant devrait commencé par un 'M'", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 15, pady = 10)

    bouton_pour_quitter = Button(interface_pour_identifiant_par_m, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_identifiant_par_m.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 15, pady = 10)

    interface_pour_identifiant_par_m.mainloop()


def au_moins_chiffre():
    interface_pour_au_moins_chiffre = Tk()
    interface_pour_au_moins_chiffre.title(string = "GesMag")
    interface_pour_au_moins_chiffre.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_au_moins_chiffre.winfo_screenwidth()
    fenetre_hauteur = interface_pour_au_moins_chiffre.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_au_moins_chiffre.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_au_moins_chiffre = Label(interface_pour_au_moins_chiffre, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_au_moins_chiffre.grid(row = 0, columnspan = 2, padx = 85, pady = 10)

    label_pour_message_alerte = Label(interface_pour_au_moins_chiffre, text = "Au moins un chiffre", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 85, pady = 10)

    bouton_pour_quitter = Button(interface_pour_au_moins_chiffre, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_au_moins_chiffre.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 85, pady = 10)

    interface_pour_au_moins_chiffre.mainloop()


def cinq_caracteres_mini():
    interface_pour_5_caracteres_maxi = Tk()
    interface_pour_5_caracteres_maxi.title(string = "GesMag")
    interface_pour_5_caracteres_maxi.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_5_caracteres_maxi.winfo_screenwidth()
    fenetre_hauteur = interface_pour_5_caracteres_maxi.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_5_caracteres_maxi.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_5_caracteres_maxi = Label(interface_pour_5_caracteres_maxi, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_5_caracteres_maxi.grid(row = 0, columnspan = 2, padx = 75, pady = 10)

    label_pour_message_alerte = Label(interface_pour_5_caracteres_maxi, text = "5 caractères minimum", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 75, pady = 10)

    bouton_pour_quitter = Button(interface_pour_5_caracteres_maxi, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_5_caracteres_maxi.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 75, pady = 10)

    interface_pour_5_caracteres_maxi.mainloop()


def saisissez_un_nom():
    interface_pour_saisissez_un_nom = Tk()
    interface_pour_saisissez_un_nom.title(string = "GesMag")
    interface_pour_saisissez_un_nom.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_saisissez_un_nom.winfo_screenwidth()
    fenetre_hauteur = interface_pour_saisissez_un_nom.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_saisissez_un_nom.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_saisissez_un_nom = Label(interface_pour_saisissez_un_nom, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_saisissez_un_nom.grid(row = 0, columnspan = 2, padx = 91, pady = 10)

    label_pour_message_alerte = Label(interface_pour_saisissez_un_nom, text = "Saisissez un nom", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 91, pady = 10)

    bouton_pour_quitter = Button(interface_pour_saisissez_un_nom, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_saisissez_un_nom.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 91, pady = 10)

    interface_pour_saisissez_un_nom.mainloop()


def pas_de_chiffres():
    interface_pour_pas_de_chiffres = Tk()
    interface_pour_pas_de_chiffres.title(string = "GesMag")
    interface_pour_pas_de_chiffres.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_pas_de_chiffres.winfo_screenwidth()
    fenetre_hauteur = interface_pour_pas_de_chiffres.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_pas_de_chiffres.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_pas_de_chiffres = Label(interface_pour_pas_de_chiffres, text = "Erreur", font = ('Arial', 12, 'bold'), bg = '#FF0000', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_pas_de_chiffres.grid(row = 0, columnspan = 2, padx = 100, pady = 10)

    label_pour_message_erreur = Label(interface_pour_pas_de_chiffres, text = "Pas de chiffres", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_erreur.grid(row = 1, columnspan = 2, padx = 100, pady = 10)

    bouton_pour_quitter = Button(interface_pour_pas_de_chiffres, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_pas_de_chiffres.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 100, pady = 10)

    interface_pour_pas_de_chiffres.mainloop()


def nom_en_majuscule():
    interface_pour_nom_en_majuscule = Tk()
    interface_pour_nom_en_majuscule.title(string = "GesMag")
    interface_pour_nom_en_majuscule.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_nom_en_majuscule.winfo_screenwidth()
    fenetre_hauteur = interface_pour_nom_en_majuscule.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_nom_en_majuscule.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_nom_en_majuscule = Label(interface_pour_nom_en_majuscule, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_nom_en_majuscule.grid(row = 0, columnspan = 2, padx = 93, pady = 10)

    label_pour_message_alerte = Label(interface_pour_nom_en_majuscule, text = "Nom en majuscle", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 93, pady = 10)

    bouton_pour_quitter = Button(interface_pour_nom_en_majuscule, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_nom_en_majuscule.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 93, pady = 10)

    interface_pour_nom_en_majuscule.mainloop()


def saisissez_un_prenom():
    interface_pour_saisissez_un_prenom = Tk()
    interface_pour_saisissez_un_prenom.title(string = "GesMag")
    interface_pour_saisissez_un_prenom.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_saisissez_un_prenom.winfo_screenwidth()
    fenetre_hauteur = interface_pour_saisissez_un_prenom.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_saisissez_un_prenom.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_saisissez_un_prenom = Label(interface_pour_saisissez_un_prenom, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_saisissez_un_prenom.grid(row = 0, columnspan = 2, padx = 80, pady = 10)

    label_pour_message_alerte = Label(interface_pour_saisissez_un_prenom, text = "Saisissez un prénom", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 80, pady = 10)

    bouton_pour_quitter = Button(interface_pour_saisissez_un_prenom, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_saisissez_un_prenom.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 80, pady = 10)

    interface_pour_saisissez_un_prenom.mainloop()


def prenom_en_minuscle():
    interface_pour_prenom_en_minuscle = Tk()
    interface_pour_prenom_en_minuscle.title(string = "GesMag")
    interface_pour_prenom_en_minuscle.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_prenom_en_minuscle.winfo_screenwidth()
    fenetre_hauteur = interface_pour_prenom_en_minuscle.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_prenom_en_minuscle.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_prenom_en_minuscle = Label(interface_pour_prenom_en_minuscle, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_prenom_en_minuscle.grid(row = 0, columnspan = 2, padx = 24, pady = 10)

    label_pour_message_alerte = Label(interface_pour_prenom_en_minuscle, text = "Prenom doit contenir des minuscles", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 24, pady = 10)

    bouton_pour_quitter = Button(interface_pour_prenom_en_minuscle, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_prenom_en_minuscle.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 24, pady = 10)

    interface_pour_prenom_en_minuscle.mainloop()


def prenom_commence_par_majuscle():
    interface_pour_prenom_commence_par_majuscle = Tk()
    interface_pour_prenom_commence_par_majuscle.title(string = "GesMag")
    interface_pour_prenom_commence_par_majuscle.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_prenom_commence_par_majuscle.winfo_screenwidth()
    fenetre_hauteur = interface_pour_prenom_commence_par_majuscle.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_prenom_commence_par_majuscle.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_prenom_commence_par_majuscle = Label(interface_pour_prenom_commence_par_majuscle, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_prenom_commence_par_majuscle.grid(row = 0, columnspan = 2, padx = 4, pady = 10)

    label_pour_message_alerte = Label(interface_pour_prenom_commence_par_majuscle, text = "Prénom doit commencé par une majuscle", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 4, pady = 10)

    bouton_pour_quitter = Button(interface_pour_prenom_commence_par_majuscle, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_prenom_commence_par_majuscle.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 4, pady = 10)

    interface_pour_prenom_commence_par_majuscle.mainloop()


def saisissez_une_date():
    interface_pour_saisissez_une_date = Tk()
    interface_pour_saisissez_une_date.title(string = "GesMag")
    interface_pour_saisissez_une_date.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_saisissez_une_date.winfo_screenwidth()
    fenetre_hauteur = interface_pour_saisissez_une_date.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_saisissez_une_date.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_saisissez_une_date = Label(interface_pour_saisissez_une_date, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_saisissez_une_date.grid(row = 0, columnspan = 2, padx = 37, pady = 10)

    label_pour_message_alerte = Label(interface_pour_saisissez_une_date, text = "Saisissez une date de naissance", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 37, pady = 10)

    bouton_pour_quitter = Button(interface_pour_saisissez_une_date, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_saisissez_une_date.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 37, pady = 10)

    interface_pour_saisissez_une_date.mainloop()


def pas_de_majuscles():
    interface_pour_pas_de_majuscles = Tk()
    interface_pour_pas_de_majuscles.title(string = "GesMag")
    interface_pour_pas_de_majuscles.configure(bg = 'white')
    x = 325
    y = 145


    fenetre_largeur = interface_pour_pas_de_majuscles.winfo_screenwidth()
    fenetre_hauteur = interface_pour_pas_de_majuscles.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_pas_de_majuscles.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_pas_de_majuscles = Label(interface_pour_pas_de_majuscles, text = "Erreur", font = ('Arial', 12, 'bold'), bg = '#FF0000', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_pas_de_majuscles.grid(row = 0, columnspan = 2, padx = 90, pady = 10)

    label_pour_message_erreur = Label(interface_pour_pas_de_majuscles, text = "Pas de majuscles", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_erreur.grid(row = 1, columnspan = 2, padx = 90, pady = 10)

    bouton_pour_quitter = Button(interface_pour_pas_de_majuscles, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_pas_de_majuscles.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 90, pady = 10)

    interface_pour_pas_de_majuscles.mainloop()


def entre_1_et_31():
    interface_pour_entre_1_et_31 = Tk()
    interface_pour_entre_1_et_31.title(string = "GesMag")
    interface_pour_entre_1_et_31.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_entre_1_et_31.winfo_screenwidth()
    fenetre_hauteur = interface_pour_entre_1_et_31.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_entre_1_et_31.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_entre_1_et_31 = Label(interface_pour_entre_1_et_31, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_entre_1_et_31.grid(row = 0, columnspan = 2, padx = 42, pady = 10)

    label_pour_message_alerte = Label(interface_pour_entre_1_et_31, text = "1 nombre compris entre 1 et 31", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 42, pady = 10)

    bouton_pour_quitter = Button(interface_pour_entre_1_et_31, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_entre_1_et_31.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 42, pady = 10)

    interface_pour_entre_1_et_31.mainloop()


def entre_1_et_12():
    interface_pour_entre_1_et_12 = Tk()
    interface_pour_entre_1_et_12.title(string = "GesMag")
    interface_pour_entre_1_et_12.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_entre_1_et_12.winfo_screenwidth()
    fenetre_hauteur = interface_pour_entre_1_et_12.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_entre_1_et_12.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_entre_1_et_12 = Label(interface_pour_entre_1_et_12, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_entre_1_et_12.grid(row = 0, columnspan = 2, padx = 42, pady = 10)

    label_pour_message_alerte = Label(interface_pour_entre_1_et_12, text = "1 nombre compris entre 1 et 12", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 42, pady = 10)

    bouton_pour_quitter = Button(interface_pour_entre_1_et_12, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_entre_1_et_12.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 42, pady = 10)

    interface_pour_entre_1_et_12.mainloop()


def nombre_a_4():
    interface_pour_nombre_a_4 = Tk()
    interface_pour_nombre_a_4.title(string = "GesMag")
    interface_pour_nombre_a_4.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_nombre_a_4.winfo_screenwidth()
    fenetre_hauteur = interface_pour_nombre_a_4.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_nombre_a_4.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_nombre_a_4 = Label(interface_pour_nombre_a_4, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_nombre_a_4.grid(row = 0, columnspan = 2, padx = 81, pady = 10)

    label_pour_message_alerte = Label(interface_pour_nombre_a_4, text = "1 nombre à 4 chiffres", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 81, pady = 10)

    bouton_pour_quitter = Button(interface_pour_nombre_a_4, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_nombre_a_4.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 81, pady = 10)

    interface_pour_nombre_a_4.mainloop()


def saisissez_une_adresse():
    interface_pour_saisissez_une_adresse = Tk()
    interface_pour_saisissez_une_adresse.title(string = "GesMag")
    interface_pour_saisissez_une_adresse.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_saisissez_une_adresse.winfo_screenwidth()
    fenetre_hauteur = interface_pour_saisissez_une_adresse.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_saisissez_une_adresse.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_saisissez_une_adresse = Label(interface_pour_saisissez_une_adresse, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_saisissez_une_adresse.grid(row = 0, columnspan = 2, padx = 75, pady = 10)

    label_pour_message_alerte = Label(interface_pour_saisissez_une_adresse, text = "Saisissez une adresse", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 75, pady = 10)

    bouton_pour_quitter = Button(interface_pour_saisissez_une_adresse, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_saisissez_une_adresse.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 75, pady = 10)

    interface_pour_saisissez_une_adresse.mainloop()


def saisissez_un_code_postal():
    interface_pour_saisissez_un_code_postal = Tk()
    interface_pour_saisissez_un_code_postal.title(string = "GesMag")
    interface_pour_saisissez_un_code_postal.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_saisissez_un_code_postal.winfo_screenwidth()
    fenetre_hauteur = interface_pour_saisissez_un_code_postal.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_saisissez_un_code_postal.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_saisissez_un_code_postal = Label(interface_pour_saisissez_un_code_postal, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_saisissez_un_code_postal.grid(row = 0, columnspan = 2, padx = 65, pady = 10)

    label_pour_message_alerte = Label(interface_pour_saisissez_un_code_postal, text = "Saisissez un code postal", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 65, pady = 10)

    bouton_pour_quitter = Button(interface_pour_saisissez_un_code_postal, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_saisissez_un_code_postal.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 65, pady = 10)

    interface_pour_saisissez_un_code_postal.mainloop()


def nombre_a_5():
    interface_pour_nombre_a_5 = Tk()
    interface_pour_nombre_a_5.title(string = "GesMag")
    interface_pour_nombre_a_5.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_nombre_a_5.winfo_screenwidth()
    fenetre_hauteur = interface_pour_nombre_a_5.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_nombre_a_5.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_nombre_a_5 = Label(interface_pour_nombre_a_5, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_nombre_a_5.grid(row = 0, columnspan = 2, padx = 81, pady = 10)

    label_pour_message_alerte = Label(interface_pour_nombre_a_5, text = "1 nombre à 5 chiffres", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 81, pady = 10)

    bouton_pour_quitter = Button(interface_pour_nombre_a_5, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_nombre_a_5.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 81, pady = 10)

    interface_pour_nombre_a_5.mainloop()


def saisissez_un_mot_de_passe():
    interface_pour_saisissez_un_mot_de_passe = Tk()
    interface_pour_saisissez_un_mot_de_passe.title(string = "GesMag")
    interface_pour_saisissez_un_mot_de_passe.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_saisissez_un_mot_de_passe.winfo_screenwidth()
    fenetre_hauteur = interface_pour_saisissez_un_mot_de_passe.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_saisissez_un_mot_de_passe.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_saisissez_un_mot_de_passe = Label(interface_pour_saisissez_un_mot_de_passe, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_saisissez_un_mot_de_passe.grid(row = 0, columnspan = 2, padx = 60, pady = 10)

    label_pour_message_alerte = Label(interface_pour_saisissez_un_mot_de_passe, text = "Saisissez un mot de passe", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 60, pady = 10)

    bouton_pour_quitter = Button(interface_pour_saisissez_un_mot_de_passe, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_saisissez_un_mot_de_passe.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 60, pady = 10)

    interface_pour_saisissez_un_mot_de_passe.mainloop()


def au_moins_un_caractere_special():
    interface_pour_au_moins_un_caractere_special = Tk()
    interface_pour_au_moins_un_caractere_special.title(string = "GesMag")
    interface_pour_au_moins_un_caractere_special.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_au_moins_un_caractere_special.winfo_screenwidth()
    fenetre_hauteur = interface_pour_au_moins_un_caractere_special.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_au_moins_un_caractere_special.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_au_moins_un_caractere_special = Label(interface_pour_au_moins_un_caractere_special, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_au_moins_un_caractere_special.grid(row = 0, columnspan = 2, padx = 45, pady = 10)

    label_pour_message_alerte = Label(interface_pour_au_moins_un_caractere_special, text = "Au moins un caractère spécial", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 45, pady = 10)

    bouton_pour_quitter = Button(interface_pour_au_moins_un_caractere_special, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_au_moins_un_caractere_special.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 45, pady = 10)

    interface_pour_au_moins_un_caractere_special.mainloop()


def au_moins_une_majuscule():
    interface_pour_au_moins_une_majuscule = Tk()
    interface_pour_au_moins_une_majuscule.title(string = "GesMag")
    interface_pour_au_moins_une_majuscule.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_au_moins_une_majuscule.winfo_screenwidth()
    fenetre_hauteur = interface_pour_au_moins_une_majuscule.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_au_moins_une_majuscule.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_au_moins_une_majuscule = Label(interface_pour_au_moins_une_majuscule, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_au_moins_une_majuscule.grid(row = 0, columnspan = 2, padx = 65, pady = 10)

    label_pour_message_alerte = Label(interface_pour_au_moins_une_majuscule, text = "Au moins une majuscule", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 65, pady = 10)

    bouton_pour_quitter = Button(interface_pour_au_moins_une_majuscule, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_au_moins_une_majuscule.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 65, pady = 10)

    interface_pour_au_moins_une_majuscule.mainloop()


def au_moins_une_minuscule():
    interface_pour_au_moins_une_minuscule = Tk()
    interface_pour_au_moins_une_minuscule.title(string = "GesMag")
    interface_pour_au_moins_une_minuscule.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_au_moins_une_minuscule.winfo_screenwidth()
    fenetre_hauteur = interface_pour_au_moins_une_minuscule.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_au_moins_une_minuscule.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_au_moins_une_minuscule = Label(interface_pour_au_moins_une_minuscule, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_au_moins_une_minuscule.grid(row = 0, columnspan = 2, padx = 65, pady = 10)

    label_pour_message_alerte = Label(interface_pour_au_moins_une_minuscule, text = "Au moins une minuscule", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 65, pady = 10)

    bouton_pour_quitter = Button(interface_pour_au_moins_une_minuscule, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_au_moins_une_minuscule.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 65, pady = 10)

    interface_pour_au_moins_une_minuscule.mainloop()


def au_moins_un_chiffre():
    interface_pour_au_moins_un_chiffre = Tk()
    interface_pour_au_moins_un_chiffre.title(string = "GesMag")
    interface_pour_au_moins_un_chiffre.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_au_moins_un_chiffre.winfo_screenwidth()
    fenetre_hauteur = interface_pour_au_moins_un_chiffre.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_au_moins_un_chiffre.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_au_moins_un_chiffre = Label(interface_pour_au_moins_un_chiffre, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_au_moins_un_chiffre.grid(row = 0, columnspan = 2, padx = 85, pady = 10)

    label_pour_message_alerte = Label(interface_pour_au_moins_un_chiffre, text = "Au moins un chiffre", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 85, pady = 10)

    bouton_pour_quitter = Button(interface_pour_au_moins_un_chiffre, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_au_moins_un_chiffre.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 85, pady = 10)

    interface_pour_au_moins_un_chiffre.mainloop()


def au_moins_8_caracteres():
    interface_pour_au_moins_8_caracteres = Tk()
    interface_pour_au_moins_8_caracteres.title(string = "GesMag")
    interface_pour_au_moins_8_caracteres.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_au_moins_8_caracteres.winfo_screenwidth()
    fenetre_hauteur = interface_pour_au_moins_8_caracteres.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_au_moins_8_caracteres.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_au_moins_8_caracteres = Label(interface_pour_au_moins_8_caracteres, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_au_moins_8_caracteres.grid(row = 0, columnspan = 2, padx = 75, pady = 10)

    label_pour_message_alerte = Label(interface_pour_au_moins_8_caracteres, text = "Au moins 8 caractères", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_alerte.grid(row = 1, columnspan = 2, padx = 75, pady = 10)

    bouton_pour_quitter = Button(interface_pour_au_moins_8_caracteres, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_au_moins_8_caracteres.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 75, pady = 10)

    interface_pour_au_moins_8_caracteres.mainloop()


def identifiant_existe_deja():
    interface_pour_identifiant_existe_deja = Tk()
    interface_pour_identifiant_existe_deja.title(string = "GesMag")
    interface_pour_identifiant_existe_deja.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_identifiant_existe_deja.winfo_screenwidth()
    fenetre_hauteur = interface_pour_identifiant_existe_deja.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_identifiant_existe_deja.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_identifiant_existe_deja = Label(interface_pour_identifiant_existe_deja, text = "Erreur", font = ('Arial', 12, 'bold'), bg = '#FF0000', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_identifiant_existe_deja.grid(row = 0, columnspan = 2, padx = 8, pady = 10)

    label_pour_message_erreur = Label(interface_pour_identifiant_existe_deja, text = "Identifiant existe déjà, saisissez un autre", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_erreur.grid(row = 1, columnspan = 2, padx = 8, pady = 10)

    bouton_pour_quitter = Button(interface_pour_identifiant_existe_deja, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_identifiant_existe_deja.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 8, pady = 10)

    interface_pour_identifiant_existe_deja.mainloop()


def mot_de_passe_existe_deja():
    interface_pour_mot_de_passe_existe_deja = Tk()
    interface_pour_mot_de_passe_existe_deja.title(string = "GesMag")
    interface_pour_mot_de_passe_existe_deja.configure(bg = 'white')

    x = 340
    y = 145


    fenetre_largeur = interface_pour_mot_de_passe_existe_deja.winfo_screenwidth()
    fenetre_hauteur = interface_pour_mot_de_passe_existe_deja.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_mot_de_passe_existe_deja.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_mot_de_passe_existe_deja = Label(interface_pour_mot_de_passe_existe_deja, text = "Erreur", font = ('Arial', 12, 'bold'), bg = '#FF0000', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_mot_de_passe_existe_deja.grid(row = 0, columnspan = 2, padx = 2, pady = 10)

    label_pour_message_erreur = Label(interface_pour_mot_de_passe_existe_deja, text = "Mot de passe existe déjà, saisissez un autre", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_erreur.grid(row = 1, columnspan = 2, padx = 2, pady = 10)

    bouton_pour_quitter = Button(interface_pour_mot_de_passe_existe_deja, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_mot_de_passe_existe_deja.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 2, pady = 10)

    interface_pour_mot_de_passe_existe_deja.mainloop()


def enregistre_avec_succes():
    interface_pour_enregistre_avec_succes = Tk()
    interface_pour_enregistre_avec_succes.title(string = "GesMag")
    interface_pour_enregistre_avec_succes.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_enregistre_avec_succes.winfo_screenwidth()
    fenetre_hauteur = interface_pour_enregistre_avec_succes.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_enregistre_avec_succes.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_enregistre_avec_succes = Label(interface_pour_enregistre_avec_succes, text = "Info", font = ('Arial', 12, 'bold'), bg = '#0080FF', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_enregistre_avec_succes.grid(row = 0, columnspan = 2, padx = 70, pady = 10)

    label_pour_message_erreur = Label(interface_pour_enregistre_avec_succes, text = "Enregistré avec succès", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_erreur.grid(row = 1, columnspan = 2, padx = 70, pady = 10)

    bouton_pour_quitter = Button(interface_pour_enregistre_avec_succes, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_enregistre_avec_succes.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 70, pady = 10)

    interface_pour_enregistre_avec_succes.mainloop()



def supprime_avec_succes():
    interface_pour_supprime_avec_succes = Tk()
    interface_pour_supprime_avec_succes.title(string = "GesMag")
    interface_pour_supprime_avec_succes.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_supprime_avec_succes.winfo_screenwidth()
    fenetre_hauteur = interface_pour_supprime_avec_succes.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_supprime_avec_succes.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_supprime_avec_succes = Label(interface_pour_supprime_avec_succes, text = "Info", font = ('Arial', 12, 'bold'), bg = '#0080FF', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_supprime_avec_succes.grid(row = 0, columnspan = 2, padx = 75, pady = 10)

    label_pour_message_erreur = Label(interface_pour_supprime_avec_succes, text = "Supprimé avec succès", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_erreur.grid(row = 1, columnspan = 2, padx = 75, pady = 10)

    bouton_pour_quitter = Button(interface_pour_supprime_avec_succes, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_supprime_avec_succes.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 75, pady = 10)

    interface_pour_supprime_avec_succes.mainloop()


def depasse_la_quantite_de_stock():
    interface_pour_depasse_la_quantite_de_stock = Tk()
    interface_pour_depasse_la_quantite_de_stock.title(string = "GesMag")
    interface_pour_depasse_la_quantite_de_stock.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_depasse_la_quantite_de_stock.winfo_screenwidth()
    fenetre_hauteur = interface_pour_depasse_la_quantite_de_stock.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_depasse_la_quantite_de_stock.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_depasse_la_quantite_de_stock = Label(interface_pour_depasse_la_quantite_de_stock, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_depasse_la_quantite_de_stock.grid(row = 0, columnspan = 2, padx = 46, pady = 10)

    label_pour_message_erreur = Label(interface_pour_depasse_la_quantite_de_stock, text = "Dépassé la quantité de stocks", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_erreur.grid(row = 1, columnspan = 2, padx = 46, pady = 10)

    bouton_pour_quitter = Button(interface_pour_depasse_la_quantite_de_stock, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_depasse_la_quantite_de_stock.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 46, pady = 10)

    interface_pour_depasse_la_quantite_de_stock.mainloop()


def pas_de_stocks():
    interface_pour_pas_de_stocks = Tk()
    interface_pour_pas_de_stocks.title(string = "GesMag")
    interface_pour_pas_de_stocks.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_pas_de_stocks.winfo_screenwidth()
    fenetre_hauteur = interface_pour_pas_de_stocks.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_pas_de_stocks.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_pas_de_stocks = Label(interface_pour_pas_de_stocks, text = "Erreur", font = ('Arial', 12, 'bold'), bg = '#FF0000', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_pas_de_stocks.grid(row = 0, columnspan = 2, padx = 110, pady = 10)

    label_pour_message_erreur = Label(interface_pour_pas_de_stocks, text = "Pas de stocks", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_erreur.grid(row = 1, columnspan = 2, padx = 110, pady = 10)

    bouton_pour_quitter = Button(interface_pour_pas_de_stocks, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_pas_de_stocks.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 110, pady = 10)

    interface_pour_pas_de_stocks.mainloop()


def saisissez_une_date1():
    interface_pour_saisissez_une_date1 = Tk()
    interface_pour_saisissez_une_date1.title(string = "GesMag")
    interface_pour_saisissez_une_date1.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_saisissez_une_date1.winfo_screenwidth()
    fenetre_hauteur = interface_pour_saisissez_une_date1.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_saisissez_une_date1.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_saisissez_une_date1 = Label(interface_pour_saisissez_une_date1, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_saisissez_une_date1.grid(row = 0, columnspan = 2, padx = 87, pady = 10)

    label_pour_message_erreur = Label(interface_pour_saisissez_une_date1, text = "Saisissez une date", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_erreur.grid(row = 1, columnspan = 2, padx = 87, pady = 10)

    bouton_pour_quitter = Button(interface_pour_saisissez_une_date1, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_saisissez_une_date1.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 87, pady = 10)

    interface_pour_saisissez_une_date1.mainloop()


def valide_avec_succes():
    interface_pour_valide_avec_succes = Tk()
    interface_pour_valide_avec_succes.title(string = "GesMag")
    interface_pour_valide_avec_succes.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_valide_avec_succes.winfo_screenwidth()
    fenetre_hauteur = interface_pour_valide_avec_succes.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_valide_avec_succes.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_valide_avec_succes = Label(interface_pour_valide_avec_succes, text = "Info", font = ('Arial', 12, 'bold'), bg = '#0080FF', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_valide_avec_succes.grid(row = 0, columnspan = 2, padx = 86, pady = 10)

    label_pour_message_erreur = Label(interface_pour_valide_avec_succes, text = "Validé avec succès", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_erreur.grid(row = 1, columnspan = 2, padx = 86, pady = 10)

    bouton_pour_quitter = Button(interface_pour_valide_avec_succes, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_valide_avec_succes.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 86, pady = 10)

    interface_pour_valide_avec_succes.mainloop()

def connectez_vous():
    interface_pour_connectez_vous = Tk()
    interface_pour_connectez_vous.title(string = "GesMag")
    interface_pour_connectez_vous.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_connectez_vous.winfo_screenwidth()
    fenetre_hauteur = interface_pour_connectez_vous.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_connectez_vous.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_connectez_vous = Label(interface_pour_connectez_vous, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_connectez_vous.grid(row = 0, columnspan = 2, padx = 98, pady = 10)

    label_pour_message_erreur = Label(interface_pour_connectez_vous, text = "Connectez-vous", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_erreur.grid(row = 1, columnspan = 2, padx = 98, pady = 10)

    bouton_pour_quitter = Button(interface_pour_connectez_vous, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_connectez_vous.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 98, pady = 10)

    interface_pour_connectez_vous.mainloop()


def saisissez_une_quantite():
    interface_pour_saisissez_une_quantite = Tk()
    interface_pour_saisissez_une_quantite.title(string = "GesMag")
    interface_pour_saisissez_une_quantite.configure(bg = 'white')

    x = 325
    y = 145


    fenetre_largeur = interface_pour_saisissez_une_quantite.winfo_screenwidth()
    fenetre_hauteur = interface_pour_saisissez_une_quantite.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_saisissez_une_quantite.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_pour_saisissez_une_quantite = Label(interface_pour_saisissez_une_quantite, text = "Alerte", font = ('Arial', 12, 'bold'), bg = '#FFBF00', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
    label_pour_saisissez_une_quantite.grid(row = 0, columnspan = 2, padx = 75, pady = 10)

    label_pour_message_erreur = Label(interface_pour_saisissez_une_quantite, text = "Saisissez une quantité", font = ('Arial', 12, 'bold'), bg = 'white')
    label_pour_message_erreur.grid(row = 1, columnspan = 2, padx = 75, pady = 10)

    bouton_pour_quitter = Button(interface_pour_saisissez_une_quantite, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = interface_pour_saisissez_une_quantite.destroy)
    bouton_pour_quitter.grid(row = 2, columnspan = 2, padx = 75, pady = 10)

    interface_pour_saisissez_une_quantite.mainloop()