from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
from interface_pour_fruits_legumes import fruits_legumes
from interface_pour_boulangerie import boulangerie
from interface_pour_boucherie_poissonnerie import boucherie_poissonnerie
from interface_pour_produits_entretien import produits_entretien

def affichage_de_stocks():
    interface_pour_afficher_les_stocks = Tk()
    interface_pour_afficher_les_stocks.title(string = "GesMag")
    interface_pour_afficher_les_stocks.configure(bg = 'white')

    x = 750
    y = 560

    fenetre_largeur = interface_pour_afficher_les_stocks.winfo_screenwidth()
    fenetre_hauteur = interface_pour_afficher_les_stocks.winfo_screenheight()

    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)

    interface_pour_afficher_les_stocks.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_affichage_de_stocks = Label(interface_pour_afficher_les_stocks, text = "Affichage des stocks", font = ('Arial', 15, 'bold'), fg = 'white', bg = '#375D81', width = 22, height = 1, bd = 3, relief = 'groove')
    label_affichage_de_stocks.grid(row = 0, columnspan = 2, pady = 10)

    img1 = Image.open("photos/legumes.jpeg", "r")
    img1 = img1.resize((300,188), Image.ANTIALIAS)
    img1.save("photos/legumes.jpeg", "jpeg")
    new_img1 = ImageTk.PhotoImage(master = interface_pour_afficher_les_stocks, file = "photos/legumes.jpeg")
    bouton_pour_fruits_legumes = Button(interface_pour_afficher_les_stocks, image = new_img1, cursor = 'hand2', command = fruits_legumes)
    bouton_pour_fruits_legumes.grid(row = 1, column = 0, padx = 35, pady = 10)

    img2 = Image.open("photos/boulangerie.jpeg", "r")
    img2 = img2.resize((300,188), Image.ANTIALIAS)
    img2.save("photos/boulangerie.jpeg", "jpeg")
    new_img2 = ImageTk.PhotoImage(master = interface_pour_afficher_les_stocks, file = "photos/boulangerie.jpeg")
    bouton_pour_boulangerie = Button(interface_pour_afficher_les_stocks, image = new_img2, cursor = 'hand2', command = boulangerie)
    bouton_pour_boulangerie.grid(row = 1, column = 1, padx = 35, pady = 10)

    img3 = Image.open("photos/boucherie.jpeg", "r")
    img3 = img3.resize((300,188), Image.ANTIALIAS)
    img3.save("photos/boucherie.jpeg", "jpeg")
    new_img3 = ImageTk.PhotoImage(master = interface_pour_afficher_les_stocks, file = "photos/boucherie.jpeg")
    bouton_pour_boucherie_poissonnerie = Button(interface_pour_afficher_les_stocks, image = new_img3, cursor = 'hand2', command = boucherie_poissonnerie)
    bouton_pour_boucherie_poissonnerie.grid(row = 2, column = 0, padx = 35, pady = 10)

    img4 = Image.open("photos/produit.jpeg", "r")
    img4 = img4.resize((300,188), Image.ANTIALIAS)
    img4.save("photos/produit.jpeg", "jpeg")
    new_img4 = ImageTk.PhotoImage(master = interface_pour_afficher_les_stocks, file = "photos/produit.jpeg")
    bouton_pour_produits_entretien = Button(interface_pour_afficher_les_stocks, image = new_img4, cursor = 'hand2', command = produits_entretien)
    bouton_pour_produits_entretien.grid(row = 2, column = 1, padx = 35, pady = 10)

    def quitter():
        interface_pour_afficher_les_stocks.destroy()

    bouton_pour_quitter = Button(interface_pour_afficher_les_stocks, text = "Quitter", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#F32665', activebackground = '#F32665', activeforeground = 'white', cursor = 'hand2', command = quitter)
    bouton_pour_quitter.grid(row = 3, columnspan = 2, pady = 30)

    interface_pour_afficher_les_stocks.mainloop()