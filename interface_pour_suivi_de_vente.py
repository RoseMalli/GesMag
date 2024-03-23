from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def interface_suivi_de_vente():
    interface_pour_suivi_de_vente = Tk()
    interface_pour_suivi_de_vente.title(string = "GesMag")
    interface_pour_suivi_de_vente.configure(bg = 'white')


    x = 721
    y = 775

    fenetre_largeur = interface_pour_suivi_de_vente.winfo_screenwidth()
    fenetre_hauteur = interface_pour_suivi_de_vente.winfo_screenheight()

    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)

    interface_pour_suivi_de_vente.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_suivi_de_vente = Label(interface_pour_suivi_de_vente, text = "Suivi de vente", font = ("Arial", 15, 'bold'), fg = 'white', bg = '#375D81', width = 16, height = 1, bd = 3, relief = 'groove')
    label_suivi_de_vente.grid(row = 0, columnspan = 2, pady = 10)

    data = pd.read_excel('ticket_de_caisse.xlsx')

    frame = Frame(interface_pour_suivi_de_vente)
    frame.grid(row = 1, columnspan = 2, pady = 10)

    histogramme = plt.Figure(figsize = (9, 9), dpi = 80)
    axes = histogramme.add_subplot()
    axes.set_facecolor('#e3e3e3')
    axes.set_xlabel("Date", fontsize = 16, color = '#AF7AC5', fontweight = 'bold')
    axes.set_ylabel("Prix total", fontsize = 16, color = '#AF7AC5', fontweight = 'bold')
    graphe = FigureCanvasTkAgg(histogramme, frame)
    graphe.get_tk_widget().pack(side = LEFT, fill = BOTH, expand = True)
    data = data[["Date", "Prix total"]].groupby("Date").sum()
    data.plot(kind = 'bar', legend = True, ax = axes, color = '#420B68', )
    histogramme.tight_layout()



    #interface_pour_suivi_de_vente.mainloop()