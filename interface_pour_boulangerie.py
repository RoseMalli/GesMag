from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
import pandas as pd

def boulangerie():
    interface_pour_boulangerie = Tk()
    interface_pour_boulangerie.title(string = "GesMag")
    interface_pour_boulangerie.configure(bg = 'white')

    x = 1290
    y = 545

    fenetre_largeur = interface_pour_boulangerie.winfo_screenwidth()
    fenetre_hauteur = interface_pour_boulangerie.winfo_screenheight()

    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)

    interface_pour_boulangerie.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_affichage_de_stocks = Label(interface_pour_boulangerie, text = "Boulangerie", font = ('Arial', 15, 'bold'), fg = 'white', bg = '#375D81', width = 16, height = 1, bd = 3, relief = 'groove')
    label_affichage_de_stocks.grid(row = 0, columnspan = 6, pady = 10)

    def baguette():
        interface_pour_baguette = Tk()
        interface_pour_baguette.title("GesMag")
        interface_pour_baguette.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_baguette.winfo_screenwidth()
        fenetre_hauteur = interface_pour_baguette.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_baguette.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')
            
        tableau = ttk.Treeview(interface_pour_baguette, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BLBAGUETTE" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BLBAGUETTE"]
            tableau.insert("","end", values = ("BLBAGUETTE" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)
                
        
    photo_baguette = ImageTk.PhotoImage(master = interface_pour_boulangerie, file = "photos/baguette.jpeg")
    bouton_pour_baguette = Button(interface_pour_boulangerie, image = photo_baguette, cursor = 'hand2', command = baguette)
    bouton_pour_baguette.grid(row = 1, column = 0, padx = 35, pady = 10)

    def burger():
        interface_pour_burger = Tk()
        interface_pour_burger.title("GesMag")
        interface_pour_burger.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_burger.winfo_screenwidth()
        fenetre_hauteur = interface_pour_burger.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_burger.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_burger, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BLPBURGER" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BLPBURGER"]
            tableau.insert("","end", values = ("BLPBURGER" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_burger = ImageTk.PhotoImage(master = interface_pour_boulangerie, file = "photos/burger.jpeg")
    bouton_pour_burger = Button(interface_pour_boulangerie, image = photo_burger, cursor = 'hand2', command = burger)
    bouton_pour_burger.grid(row = 1, column = 1, padx = 35, pady = 10)

    def graincourge():
        interface_pour_graincourge = Tk()
        interface_pour_graincourge.title("GesMag")
        interface_pour_graincourge.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_graincourge.winfo_screenwidth()
        fenetre_hauteur = interface_pour_graincourge.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_graincourge.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_graincourge, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BLPGRAINCOURGE" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BLPGRAINCOURGE"]
            tableau.insert("","end", values = ("BLPGRAINCOURGE" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_graincourge = ImageTk.PhotoImage(master = interface_pour_boulangerie, file = "photos/graincourge.jpeg")
    bouton_pour_graincourge = Button(interface_pour_boulangerie, image = photo_graincourge, cursor = 'hand2', command = graincourge)
    bouton_pour_graincourge.grid(row = 1, column = 2, padx = 35, pady = 10)

    def chaussonpomme():
        interface_pour_chaussonpomme = Tk()
        interface_pour_chaussonpomme.title("GesMag")
        interface_pour_chaussonpomme.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_chaussonpomme.winfo_screenwidth()
        fenetre_hauteur = interface_pour_chaussonpomme.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_chaussonpomme.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_chaussonpomme, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BLCHAUSSON" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BLCHAUSSON"]
            tableau.insert("","end", values = ("BLCHAUSSON" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_chaussonpomme = ImageTk.PhotoImage(master = interface_pour_boulangerie, file = "photos/chaussonpomme.jpeg")
    bouton_pour_chaussonpomme = Button(interface_pour_boulangerie, image = photo_chaussonpomme, cursor = 'hand2', command = chaussonpomme)
    bouton_pour_chaussonpomme.grid(row = 1, column = 3, padx = 35, pady = 10)

    def nordique():
        interface_pour_nordique = Tk()
        interface_pour_nordique.title("GesMag")
        interface_pour_nordique.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_nordique.winfo_screenwidth()
        fenetre_hauteur = interface_pour_nordique.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_nordique.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_nordique, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BLPNORDIQUE" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BLPNORDIQUE"]
            tableau.insert("","end", values = ("BLPNORDIQUE" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_nordique = ImageTk.PhotoImage(master = interface_pour_boulangerie, file = "photos/nordique.jpeg")
    bouton_pour_nordique = Button(interface_pour_boulangerie, image = photo_nordique, cursor = 'hand2', command = nordique)
    bouton_pour_nordique.grid(row = 1, column = 4, padx = 35, pady = 10)

    def croissant():
        interface_pour_croissant = Tk()
        interface_pour_croissant.title("GesMag")
        interface_pour_croissant.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_croissant.winfo_screenwidth()
        fenetre_hauteur = interface_pour_croissant.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_croissant.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_croissant, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BLCROISSANT" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BLCROISSANT"]
            tableau.insert("","end", values = ("BLCROISSANT" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_croissant = ImageTk.PhotoImage(master = interface_pour_boulangerie, file = "photos/croissant.jpeg")
    bouton_pour_croissant = Button(interface_pour_boulangerie, image = photo_croissant, cursor = 'hand2', command = croissant)
    bouton_pour_croissant.grid(row = 2, column = 0, padx = 35, pady = 10)

    def chocolat():
        interface_pour_chocolat = Tk()
        interface_pour_chocolat.title("GesMag")
        interface_pour_chocolat.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_chocolat.winfo_screenwidth()
        fenetre_hauteur = interface_pour_chocolat.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_chocolat.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_chocolat, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BLPCHOCOLAT" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BLPCHOCOLAT"]
            tableau.insert("","end", values = ("BLPCHOCOLAT" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_chocolat = ImageTk.PhotoImage(master = interface_pour_boulangerie, file = "photos/chocolat.jpeg")
    bouton_pour_chocolat = Button(interface_pour_boulangerie, image = photo_chocolat, cursor = 'hand2', command = chocolat)
    bouton_pour_chocolat.grid(row = 2, column = 1, padx = 35, pady = 10)

    def mie():
        interface_pour_mie = Tk()
        interface_pour_mie.title("GesMag")
        interface_pour_mie.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_mie.winfo_screenwidth()
        fenetre_hauteur = interface_pour_mie.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_mie.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_mie, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BLPMIE" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BLPMIE"]
            tableau.insert("","end", values = ("BLPMIE" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_mie = ImageTk.PhotoImage(master = interface_pour_boulangerie, file = "photos/mie.jpeg")
    bouton_pour_mie = Button(interface_pour_boulangerie, image = photo_mie, cursor = 'hand2', command = mie)
    bouton_pour_mie.grid(row = 2, column = 2, padx = 35, pady = 10)

    def campagne():
        interface_pour_campagne = Tk()
        interface_pour_campagne.title("GesMag")
        interface_pour_campagne.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_campagne.winfo_screenwidth()
        fenetre_hauteur = interface_pour_campagne.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_campagne.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_campagne, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BLPCAMPAGNE" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BLPCAMPAGNE"]
            tableau.insert("","end", values = ("BLPCAMPAGNE" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_campagne = ImageTk.PhotoImage(master = interface_pour_boulangerie, file = "photos/campagne.jpeg")
    bouton_pour_campagne = Button(interface_pour_boulangerie, image = photo_campagne, cursor = 'hand2', command = campagne)
    bouton_pour_campagne.grid(row = 2, column = 3, padx = 35, pady = 10)

    def croquant():
        interface_pour_croquant = Tk()
        interface_pour_croquant.title("GesMag")
        interface_pour_croquant.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_croquant.winfo_screenwidth()
        fenetre_hauteur = interface_pour_croquant.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_croquant.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_croquant, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BLPCROQAMANDE" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BLPCROQAMANDE"]
            tableau.insert("","end", values = ("BLPCROQAMANDE" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)


    photo_croquant = ImageTk.PhotoImage(master = interface_pour_boulangerie, file = "photos/croquantamande.jpeg")
    bouton_pour_croquant = Button(interface_pour_boulangerie, image = photo_croquant, cursor = 'hand2', command = croquant)
    bouton_pour_croquant.grid(row = 2, column = 4, padx = 35, pady = 10)

    def quitter():
        interface_pour_boulangerie.destroy()

    bouton_pour_quitter = Button(interface_pour_boulangerie, text = "Quitter", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#F32665', activebackground = '#F32665', activeforeground = 'white', cursor = 'hand2', command = quitter)
    bouton_pour_quitter.grid(row = 3, columnspan = 6, pady = 30)

    interface_pour_boulangerie.mainloop()