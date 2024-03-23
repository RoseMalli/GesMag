from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
import pandas as pd

def produits_entretien():
    interface_pour_produits_entretien = Tk()
    interface_pour_produits_entretien.title(string = "GesMag")
    interface_pour_produits_entretien.configure(bg = 'white')

    x = 1290
    y = 545

    fenetre_largeur = interface_pour_produits_entretien.winfo_screenwidth()
    fenetre_hauteur = interface_pour_produits_entretien.winfo_screenheight()

    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)

    interface_pour_produits_entretien.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_affichage_de_stocks = Label(interface_pour_produits_entretien, text = "Produits d'entretien", font = ('Arial', 15, 'bold'), fg = 'white', bg = '#375D81', width = 21, height = 1, bd = 3, relief = 'groove')
    label_affichage_de_stocks.grid(row = 0, columnspan = 6, pady = 10)

    def cif():
        interface_pour_cif = Tk()
        interface_pour_cif.title("GesMag")
        interface_pour_cif.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_cif.winfo_screenwidth()
        fenetre_hauteur = interface_pour_cif.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_cif.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')
            
        tableau = ttk.Treeview(interface_pour_cif, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "PECIFCMS" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["PECIFCMS"]
            tableau.insert("","end", values = ("PECIFCMS" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)
                
        
    photo_cif = ImageTk.PhotoImage(master = interface_pour_produits_entretien, file = "photos/cif.jpeg")
    bouton_pour_cif = Button(interface_pour_produits_entretien, image = photo_cif, cursor = 'hand2', command = cif)
    bouton_pour_cif.grid(row = 1, column = 0, padx = 35, pady = 10)

    def vaisselle():
        interface_pour_vaisselle = Tk()
        interface_pour_vaisselle.title("GesMag")
        interface_pour_vaisselle.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_vaisselle.winfo_screenwidth()
        fenetre_hauteur = interface_pour_vaisselle.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_vaisselle.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_vaisselle, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "PEMIRLVC" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["PEMIRLVC"]
            tableau.insert("","end", values = ("PEMIRLVC" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_vaisselle = ImageTk.PhotoImage(master = interface_pour_produits_entretien, file = "photos/vaisselle.jpeg")
    bouton_pour_vaisselle = Button(interface_pour_produits_entretien, image = photo_vaisselle, cursor = 'hand2', command = vaisselle)
    bouton_pour_vaisselle.grid(row = 1, column = 1, padx = 35, pady = 10)

    def combinebrosse():
        interface_pour_combinebrosse = Tk()
        interface_pour_combinebrosse.title("GesMag")
        interface_pour_combinebrosse.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_combinebrosse.winfo_screenwidth()
        fenetre_hauteur = interface_pour_combinebrosse.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_combinebrosse.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_combinebrosse, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "PECOMBIBROWC" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["PECOMBIBROWC"]
            tableau.insert("","end", values = ("PECOMBIBROWC" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_combinebrosse = ImageTk.PhotoImage(master = interface_pour_produits_entretien, file = "photos/combinebrosse.jpeg")
    bouton_pour_combinebrosse = Button(interface_pour_produits_entretien, image = photo_combinebrosse, cursor = 'hand2', command = combinebrosse)
    bouton_pour_combinebrosse.grid(row = 1, column = 2, padx = 35, pady = 10)

    def bakingsoda():
        interface_pour_bakingsoda = Tk()
        interface_pour_bakingsoda.title("GesMag")
        interface_pour_bakingsoda.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_bakingsoda.winfo_screenwidth()
        fenetre_hauteur = interface_pour_bakingsoda.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_bakingsoda.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_bakingsoda, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "PEBIOVIEBICASOU" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["PEBIOVIEBICASOU"]
            tableau.insert("","end", values = ("PEBIOVIEBICASOU" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_bakingsoda = ImageTk.PhotoImage(master = interface_pour_produits_entretien, file = "photos/bakingsoda.jpeg")
    bouton_pour_bakingsoda = Button(interface_pour_produits_entretien, image = photo_bakingsoda, cursor = 'hand2', command = bakingsoda)
    bouton_pour_bakingsoda.grid(row = 1, column = 3, padx = 35, pady = 10)

    def sol():
        interface_pour_sol = Tk()
        interface_pour_sol.title("GesMag")
        interface_pour_sol.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_sol.winfo_screenwidth()
        fenetre_hauteur = interface_pour_sol.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_sol.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_sol, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "PEDESINFSOSUR" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["PEDESINFSOSUR"]
            tableau.insert("","end", values = ("PEDESINFSOSUR" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_sol = ImageTk.PhotoImage(master = interface_pour_produits_entretien, file = "photos/sols.jpeg")
    bouton_pour_sol = Button(interface_pour_produits_entretien, image = photo_sol, cursor = 'hand2', command = sol)
    bouton_pour_sol.grid(row = 1, column = 4, padx = 35, pady = 10)

    def lingette():
        interface_pour_lingette = Tk()
        interface_pour_lingette.title("GesMag")
        interface_pour_lingette.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_lingette.winfo_screenwidth()
        fenetre_hauteur = interface_pour_lingette.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_lingette.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_lingette, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "PELINGETTES" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["PELINGETTES"]
            tableau.insert("","end", values = ("PELINGETTES" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_lingette = ImageTk.PhotoImage(master = interface_pour_produits_entretien, file = "photos/lingette.jpeg")
    bouton_pour_lingette = Button(interface_pour_produits_entretien, image = photo_lingette, cursor = 'hand2', command = lingette)
    bouton_pour_lingette.grid(row = 2, column = 0, padx = 35, pady = 10)

    def nettoyant():
        interface_pour_nettoyant = Tk()
        interface_pour_nettoyant.title("GesMag")
        interface_pour_nettoyant.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_nettoyant.winfo_screenwidth()
        fenetre_hauteur = interface_pour_nettoyant.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_nettoyant.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_nettoyant, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "PENETTOYANTV" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["PENETTOYANTV"]
            tableau.insert("","end", values = ("PENETTOYANTV" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_nettoyant = ImageTk.PhotoImage(master = interface_pour_produits_entretien, file = "photos/nettoyant.jpeg")
    bouton_pour_nettoyant = Button(interface_pour_produits_entretien, image = photo_nettoyant, cursor = 'hand2', command = nettoyant)
    bouton_pour_nettoyant.grid(row = 2, column = 1, padx = 35, pady = 10)

    def javel():
        interface_pour_javel = Tk()
        interface_pour_javel.title("GesMag")
        interface_pour_javel.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_javel.winfo_screenwidth()
        fenetre_hauteur = interface_pour_javel.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_javel.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_javel, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "PEJAVELWC31" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["PEJAVELWC31"]
            tableau.insert("","end", values = ("PEJAVELWC31" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_javel = ImageTk.PhotoImage(master = interface_pour_produits_entretien, file = "photos/javel.jpeg")
    bouton_pour_javel = Button(interface_pour_produits_entretien, image = photo_javel, cursor = 'hand2', command = javel)
    bouton_pour_javel.grid(row = 2, column = 2, padx = 35, pady = 10)

    def lavette():
        interface_pour_lavette = Tk()
        interface_pour_lavette.title("GesMag")
        interface_pour_lavette.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_lavette.winfo_screenwidth()
        fenetre_hauteur = interface_pour_lavette.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_lavette.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_lavette, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "PELAVETTESTIS" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["PELAVETTESTIS"]
            tableau.insert("","end", values = ("PELAVETTESTIS" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)

    photo_lavette = ImageTk.PhotoImage(master = interface_pour_produits_entretien, file = "photos/lavette.jpeg")
    bouton_pour_lavette = Button(interface_pour_produits_entretien, image = photo_lavette, cursor = 'hand2', command = lavette)
    bouton_pour_lavette.grid(row = 2, column = 3, padx = 35, pady = 10)

    def gant():
        interface_pour_gant = Tk()
        interface_pour_gant.title("GesMag")
        interface_pour_gant.configure(bg = 'white')

        x = 875
        y = 65

        fenetre_largeur = interface_pour_gant.winfo_screenwidth()
        fenetre_hauteur = interface_pour_gant.winfo_screenheight()

        largeur = (fenetre_largeur / 2) - (x / 2)
        hauteur = (fenetre_hauteur / 2) - (y /2)

        interface_pour_gant.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

        tableau = ttk.Treeview(interface_pour_gant, height = 1)
        data = pd.read_excel("stocks.xlsx")
        tableau["column"] = list(data.columns)
        tableau["show"] = "headings"
        for colonne in tableau["column"]:
            tableau.heading(colonne, text = colonne)
        trouver = data["Identifiant"].values
        if "PEGANTNETTO" in trouver:
            data1 = pd.read_excel('stocks.xlsx', index_col = "Identifiant")
            searched = data1.loc["PEGANTNETTO"]
            tableau.insert("","end", values = ("PEGANTNETTO" + " " + str(searched.values)[1:-1]))
        tableau.grid(row = 0, columnspan = 2, padx = 35, pady = 10)


    photo_gant = ImageTk.PhotoImage(master = interface_pour_produits_entretien, file = "photos/gant.jpeg")
    bouton_pour_gant = Button(interface_pour_produits_entretien, image = photo_gant, cursor = 'hand2', command = gant)
    bouton_pour_gant.grid(row = 2, column = 4, padx = 35, pady = 10)

    def quitter():
        interface_pour_produits_entretien.destroy()

    bouton_pour_quitter = Button(interface_pour_produits_entretien, text = "Quitter", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#F32665', activebackground = '#F32665', activeforeground = 'white', cursor = 'hand2', command = quitter)
    bouton_pour_quitter.grid(row = 3, columnspan = 6, pady = 30)

    interface_pour_produits_entretien.mainloop()