from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
import pandas as pd

def fruits_legumes():
    interface_pour_fruits_legumes = Tk()
    interface_pour_fruits_legumes.title(string = "GesMag")
    interface_pour_fruits_legumes.configure(bg = 'white')

    x = 1290
    y = 545

    fenetre_largeur = interface_pour_fruits_legumes.winfo_screenwidth()
    fenetre_hauteur = interface_pour_fruits_legumes.winfo_screenheight()

    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)

    interface_pour_fruits_legumes.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_affichage_de_stocks = Label(interface_pour_fruits_legumes, text = "Fruits / Legumes", font = ('Arial', 15, 'bold'), fg = 'white', bg = '#375D81', width = 20, height = 1, bd = 3, relief = 'groove')
    label_affichage_de_stocks.grid(row = 0, columnspan = 6, pady = 10)

    def mangue():
        interface_pour_mangue = Tk()
        interface_pour_mangue.title("GesMag")
        interface_pour_mangue.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_mangue.winfo_screenwidth()
        fenetre_hauteur = interface_pour_mangue.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_mangue.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        
            
        tableau = ttk.Treeview(interface_pour_mangue, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "FLMANGO" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["FLMANGO"]
            tableau.insert("","end", values = ("FLMANGO" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)
                
        
    photo_mague = ImageTk.PhotoImage(master = interface_pour_fruits_legumes, file = "photos/mangue.png")
    bouton_pour_mangue = Button(interface_pour_fruits_legumes, image = photo_mague, cursor = 'hand2', command = mangue)
    bouton_pour_mangue.grid(row = 1, column = 0, padx = 35, pady = 10)

    def kiwi():
        interface_pour_kiwi = Tk()
        interface_pour_kiwi.title("GesMag")
        interface_pour_kiwi.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_kiwi.winfo_screenwidth()
        fenetre_hauteur = interface_pour_kiwi.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_kiwi.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        

        tableau = ttk.Treeview(interface_pour_kiwi, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "FLKIWI" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["FLKIWI"]
            tableau.insert("","end", values = ("FLKIWI" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_kiwi = ImageTk.PhotoImage(master = interface_pour_fruits_legumes, file = "photos/kiwi.jpeg")
    bouton_pour_kiwi = Button(interface_pour_fruits_legumes, image = photo_kiwi, cursor = 'hand2', command = kiwi)
    bouton_pour_kiwi.grid(row = 1, column = 1, padx = 35, pady = 10)

    def banane():
        interface_pour_banane = Tk()
        interface_pour_banane.title("GesMag")
        interface_pour_banane.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_banane.winfo_screenwidth()
        fenetre_hauteur = interface_pour_banane.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_banane.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        

        tableau = ttk.Treeview(interface_pour_banane, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "FLBANANA" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["FLBANANA"]
            tableau.insert("","end", values = ("FLBANANA" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_banane = ImageTk.PhotoImage(master = interface_pour_fruits_legumes, file = "photos/banane.jpeg")
    bouton_pour_banane = Button(interface_pour_fruits_legumes, image = photo_banane, cursor = 'hand2', command = banane)
    bouton_pour_banane.grid(row = 1, column = 2, padx = 35, pady = 10)

    def pomme():
        interface_pour_pomme = Tk()
        interface_pour_pomme.title("GesMag")
        interface_pour_pomme.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_pomme.winfo_screenwidth()
        fenetre_hauteur = interface_pour_pomme.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_pomme.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        

        tableau = ttk.Treeview(interface_pour_pomme, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "FLAPPLE" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["FLAPPLE"]
            tableau.insert("","end", values = ("FLAPPLE" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_pomme = ImageTk.PhotoImage(master = interface_pour_fruits_legumes, file = "photos/pomme.jpeg")
    bouton_pour_pomme = Button(interface_pour_fruits_legumes, image = photo_pomme, cursor = 'hand2', command = pomme)
    bouton_pour_pomme.grid(row = 1, column = 3, padx = 35, pady = 10)

    def raisin():
        interface_pour_raisin = Tk()
        interface_pour_raisin.title("GesMag")
        interface_pour_raisin.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_raisin.winfo_screenwidth()
        fenetre_hauteur = interface_pour_raisin.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_raisin.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        

        tableau = ttk.Treeview(interface_pour_raisin, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "FLGRAPE" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["FLGRAPE"]
            tableau.insert("","end", values = ("FLGRAPE" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_raisin = ImageTk.PhotoImage(master = interface_pour_fruits_legumes, file = "photos/raisin.jpeg")
    bouton_pour_raisin = Button(interface_pour_fruits_legumes, image = photo_raisin, cursor = 'hand2', command = raisin)
    bouton_pour_raisin.grid(row = 1, column = 4, padx = 35, pady = 10)

    def courge():
        interface_pour_courge = Tk()
        interface_pour_courge.title("GesMag")
        interface_pour_courge.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_courge.winfo_screenwidth()
        fenetre_hauteur = interface_pour_courge.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_courge.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        

        tableau = ttk.Treeview(interface_pour_courge, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "FLBUTTERNUT" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["FLBUTTERNUT"]
            tableau.insert("","end", values = ("FLBUTTERNUT" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_courge = ImageTk.PhotoImage(master = interface_pour_fruits_legumes, file = "photos/courge.jpeg")
    bouton_pour_courge = Button(interface_pour_fruits_legumes, image = photo_courge, cursor = 'hand2', command = courge)
    bouton_pour_courge.grid(row = 2, column = 0, padx = 35, pady = 10)

    def laitue():
        interface_pour_laitue = Tk()
        interface_pour_laitue.title("GesMag")
        interface_pour_laitue.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_laitue.winfo_screenwidth()
        fenetre_hauteur = interface_pour_laitue.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_laitue.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        

        tableau = ttk.Treeview(interface_pour_laitue, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "FLLETTUCE" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["FLLETTUCE"]
            tableau.insert("","end", values = ("FLLETTUCE" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_laitue = ImageTk.PhotoImage(master = interface_pour_fruits_legumes, file = "photos/laitue.jpeg")
    bouton_pour_laitue = Button(interface_pour_fruits_legumes, image = photo_laitue, cursor = 'hand2', command = laitue)
    bouton_pour_laitue.grid(row = 2, column = 1, padx = 35, pady = 10)

    def carotte():
        interface_pour_carotte = Tk()
        interface_pour_carotte.title("GesMag")
        interface_pour_carotte.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_carotte.winfo_screenwidth()
        fenetre_hauteur = interface_pour_carotte.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_carotte.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        

        tableau = ttk.Treeview(interface_pour_carotte, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "FLCARROT" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["FLCARROT"]
            tableau.insert("","end", values = ("FLCARROT" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_carotte = ImageTk.PhotoImage(master = interface_pour_fruits_legumes, file = "photos/carotte.jpeg")
    bouton_pour_carotte = Button(interface_pour_fruits_legumes, image = photo_carotte, cursor = 'hand2', command = carotte)
    bouton_pour_carotte.grid(row = 2, column = 2, padx = 35, pady = 10)

    def choux():
        interface_pour_choux = Tk()
        interface_pour_choux.title("GesMag")
        interface_pour_choux.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_choux.winfo_screenwidth()
        fenetre_hauteur = interface_pour_choux.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_choux.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        

        tableau = ttk.Treeview(interface_pour_choux, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "FLGABBAGE" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["FLGABBAGE"]
            tableau.insert("","end", values = ("FLGABBAGE" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_choux = ImageTk.PhotoImage(master = interface_pour_fruits_legumes, file = "photos/choux.jpeg")
    bouton_pour_choux = Button(interface_pour_fruits_legumes, image = photo_choux, cursor = 'hand2', command = choux)
    bouton_pour_choux.grid(row = 2, column = 3, padx = 35, pady = 10)

    def brocoli():
        interface_pour_brocoli = Tk()
        interface_pour_brocoli.title("GesMag")
        interface_pour_brocoli.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_brocoli.winfo_screenwidth()
        fenetre_hauteur = interface_pour_brocoli.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_brocoli.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        

        tableau = ttk.Treeview(interface_pour_brocoli, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "FLBROCCOLI" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["FLBROCCOLI"]
            tableau.insert("","end", values = ("FLBROCCOLI" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)


    photo_brocoli = ImageTk.PhotoImage(master = interface_pour_fruits_legumes, file = "photos/brocoli.jpeg")
    bouton_pour_brocoli = Button(interface_pour_fruits_legumes, image = photo_brocoli, cursor = 'hand2', command = brocoli)
    bouton_pour_brocoli.grid(row = 2, column = 4, padx = 35, pady = 10)

    def quitter():
        interface_pour_fruits_legumes.destroy()

    bouton_pour_quitter = Button(interface_pour_fruits_legumes, text = "Quitter", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#F32665', activebackground = '#F32665', activeforeground = 'white', cursor = 'hand2', command = quitter)
    bouton_pour_quitter.grid(row = 3, columnspan = 6, pady = 30)

    interface_pour_fruits_legumes.mainloop()