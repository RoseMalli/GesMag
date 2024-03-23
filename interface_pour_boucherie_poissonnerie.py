from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
import pandas as pd

def boucherie_poissonnerie():
    interface_pour_boucherie_poissonnerie = Tk()
    interface_pour_boucherie_poissonnerie.title(string = "GesMag")
    interface_pour_boucherie_poissonnerie.configure(bg = 'white')

    x = 1290
    y = 545


    fenetre_largeur = interface_pour_boucherie_poissonnerie.winfo_screenwidth()
    fenetre_hauteur = interface_pour_boucherie_poissonnerie.winfo_screenheight()


    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)


    interface_pour_boucherie_poissonnerie.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_affichage_de_stocks = Label(interface_pour_boucherie_poissonnerie, text = "Boucherie / Poissonnerie", font = ('Arial', 15, 'bold'), fg = 'white', bg = '#375D81', width = 25, height = 1, bd = 3, relief = 'groove')
    label_affichage_de_stocks.grid(row = 0, columnspan = 6, pady = 10)

    def boeuf():
        interface_pour_boeuf = Tk()
        interface_pour_boeuf.title("GesMag")
        interface_pour_boeuf.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_boeuf.winfo_screenwidth()
        fenetre_hauteur = interface_pour_boeuf.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_boeuf.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')
            
        tableau = ttk.Treeview(interface_pour_boeuf, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BPBOEUF" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BPBOEUF"]
            tableau.insert("","end", values = ("BPBOEUF" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)
                
        
    photo_boeuf = ImageTk.PhotoImage(master = interface_pour_boucherie_poissonnerie, file = "photos/boeuf.jpeg")
    bouton_pour_boeuf = Button(interface_pour_boucherie_poissonnerie, image = photo_boeuf, cursor = 'hand2', command = boeuf)
    bouton_pour_boeuf.grid(row = 1, column = 0, padx = 35, pady = 10)

    def blanc_de_poulet():
        interface_pour_blanc_de_poulet = Tk()
        interface_pour_blanc_de_poulet.title("GesMag")
        interface_pour_blanc_de_poulet.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_blanc_de_poulet.winfo_screenwidth()
        fenetre_hauteur = interface_pour_blanc_de_poulet.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_blanc_de_poulet.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_blanc_de_poulet, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BPBLANCPOULET" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BPBLANCPOULET"]
            tableau.insert("","end", values = ("BPBLANCPOULET" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_blanc_de_poulet = ImageTk.PhotoImage(master = interface_pour_boucherie_poissonnerie, file = "photos/blanc_poulet.jpeg")
    bouton_pour_blanc_de_poulet = Button(interface_pour_boucherie_poissonnerie, image = photo_blanc_de_poulet, cursor = 'hand2', command = blanc_de_poulet)
    bouton_pour_blanc_de_poulet.grid(row = 1, column = 1, padx = 35, pady = 10)

    def escalope():
        interface_pour_escalope = Tk()
        interface_pour_escalope.title("GesMag")
        interface_pour_escalope.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_escalope.winfo_screenwidth()
        fenetre_hauteur = interface_pour_escalope.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_escalope.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_escalope, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BPESCALOPE" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BPESCALOPE"]
            tableau.insert("","end", values = ("BPESCALOPE" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_escalope = ImageTk.PhotoImage(master = interface_pour_boucherie_poissonnerie, file = "photos/escalope.jpeg")
    bouton_pour_escalope = Button(interface_pour_boucherie_poissonnerie, image = photo_escalope, cursor = 'hand2', command = escalope)
    bouton_pour_escalope.grid(row = 1, column = 2, padx = 35, pady = 10)

    def canard():
        interface_pour_canard = Tk()
        interface_pour_canard.title("GesMag")
        interface_pour_canard.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_canard.winfo_screenwidth()
        fenetre_hauteur = interface_pour_canard.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_canard.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_canard, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BPMAGCANARD" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BPMAGCANARD"]
            tableau.insert("","end", values = ("BPMAGCANARD" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_canard = ImageTk.PhotoImage(master = interface_pour_boucherie_poissonnerie, file = "photos/canard.jpeg")
    bouton_pour_canard = Button(interface_pour_boucherie_poissonnerie, image = photo_canard, cursor = 'hand2', command = canard)
    bouton_pour_canard.grid(row = 1, column = 3, padx = 35, pady = 10)

    def porc():
        interface_pour_porc = Tk()
        interface_pour_porc.title("GesMag")
        interface_pour_porc.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_porc.winfo_screenwidth()
        fenetre_hauteur = interface_pour_porc.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_porc.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_porc, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BPPORC" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BPPORC"]
            tableau.insert("","end", values = ("BPPORC" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_porc = ImageTk.PhotoImage(master = interface_pour_boucherie_poissonnerie, file = "photos/coteporc.jpeg")
    bouton_pour_porc = Button(interface_pour_boucherie_poissonnerie, image = photo_porc, cursor = 'hand2', command = porc)
    bouton_pour_porc.grid(row = 1, column = 4, padx = 35, pady = 10)

    def crevette():
        interface_pour_crevette = Tk()
        interface_pour_crevette.title("GesMag")
        interface_pour_crevette.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_crevette.winfo_screenwidth()
        fenetre_hauteur = interface_pour_crevette.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_crevette.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_crevette, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BPCREVETTE" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BPCREVETTE"]
            tableau.insert("","end", values = ("BPCREVETTE" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_crevette = ImageTk.PhotoImage(master = interface_pour_boucherie_poissonnerie, file = "photos/crevette.png")
    bouton_pour_crevette = Button(interface_pour_boucherie_poissonnerie, image = photo_crevette, cursor = 'hand2', command = crevette)
    bouton_pour_crevette.grid(row = 2, column = 0, padx = 35, pady = 10)

    def dorade():
        interface_pour_dorade = Tk()
        interface_pour_dorade.title("GesMag")
        interface_pour_dorade.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_dorade.winfo_screenwidth()
        fenetre_hauteur = interface_pour_dorade.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_dorade.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_dorade, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BPDORADE" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BPDORADE"]
            tableau.insert("","end", values = ("BPDORADE" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_dorade = ImageTk.PhotoImage(master = interface_pour_boucherie_poissonnerie, file = "photos/dorade.jpeg")
    bouton_pour_dorade = Button(interface_pour_boucherie_poissonnerie, image = photo_dorade, cursor = 'hand2', command = dorade)
    bouton_pour_dorade.grid(row = 2, column = 1, padx = 35, pady = 10)

    def encornet():
        interface_pour_encornet = Tk()
        interface_pour_encornet.title("GesMag")
        interface_pour_encornet.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_encornet.winfo_screenwidth()
        fenetre_hauteur = interface_pour_encornet.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_encornet.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_encornet, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BPENCORNET" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BPENCORNET"]
            tableau.insert("","end", values = ("BPENCORNET" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_encornet = ImageTk.PhotoImage(master = interface_pour_boucherie_poissonnerie, file = "photos/encornet.jpeg")
    bouton_pour_encornet = Button(interface_pour_boucherie_poissonnerie, image = photo_encornet, cursor = 'hand2', command = encornet)
    bouton_pour_encornet.grid(row = 2, column = 2, padx = 35, pady = 10)

    def moule():
        interface_pour_moule = Tk()
        interface_pour_moule.title("GesMag")
        interface_pour_moule.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_moule.winfo_screenwidth()
        fenetre_hauteur = interface_pour_moule.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_moule.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_moule, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BPMOULE" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BPMOULE"]
            tableau.insert("","end", values = ("BPMOULE" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_moule = ImageTk.PhotoImage(master = interface_pour_boucherie_poissonnerie, file = "photos/moule.jpeg")
    bouton_pour_moule = Button(interface_pour_boucherie_poissonnerie, image = photo_moule, cursor = 'hand2', command = moule)
    bouton_pour_moule.grid(row = 2, column = 3, padx = 35, pady = 10)

    def thon():
        interface_pour_thon = Tk()
        interface_pour_thon.title("GesMag")
        interface_pour_thon.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_thon.winfo_screenwidth()
        fenetre_hauteur = interface_pour_thon.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_thon.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_thon, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "BPTHON" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["BPTHON"]
            tableau.insert("","end", values = ("BPTHON" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)


    photo_thon = ImageTk.PhotoImage(master = interface_pour_boucherie_poissonnerie, file = "photos/thon.jpeg")
    bouton_pour_thon = Button(interface_pour_boucherie_poissonnerie, image = photo_thon, cursor = 'hand2', command = thon)
    bouton_pour_thon.grid(row = 2, column = 4, padx = 35, pady = 10)

    def quitter():
        interface_pour_boucherie_poissonnerie.destroy()

    bouton_pour_quitter = Button(interface_pour_boucherie_poissonnerie, text = "Quitter", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#F32665', activebackground = '#F32665', activeforeground = 'white', cursor = 'hand2', command = quitter)
    bouton_pour_quitter.grid(row = 3, columnspan = 6, pady = 30)

    interface_pour_boucherie_poissonnerie.mainloop()