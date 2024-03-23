from tkinter import *
import pandas as pd
from openpyxl import *
from messages import *

def interface_suppression_caissiers_managers():
    interface_pour_supprimer_un_caissier_et_un_manager = Tk()
    interface_pour_supprimer_un_caissier_et_un_manager.geometry("525x180")
    interface_pour_supprimer_un_caissier_et_un_manager.title(string = "GesMag")
    interface_pour_supprimer_un_caissier_et_un_manager.configure(bg = 'white')

    x = 525
    y = 180

    fenetre_largeur = interface_pour_supprimer_un_caissier_et_un_manager.winfo_screenwidth()
    fenetre_hauteur = interface_pour_supprimer_un_caissier_et_un_manager.winfo_screenheight()

    largeur = (fenetre_largeur / 2) - (x / 2)
    hauteur = (fenetre_hauteur / 2) - (y /2)

    interface_pour_supprimer_un_caissier_et_un_manager.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    label_supprimer_caissier = Label(interface_pour_supprimer_un_caissier_et_un_manager, text = "Suppression des caissiers / managers", font = ("Arial", 15, 'bold'), fg = 'white', bg = '#375D81', width = 37, height = 1, bd = 3, relief = 'groove')
    label_supprimer_caissier.grid(row = 0, columnspan = 2, pady = 10)


    label_supprimer_identifiant_caissier_manager = Label(interface_pour_supprimer_un_caissier_et_un_manager, text = "Identifiant :", font = ("Arial", 12, 'bold'), bg = 'white')
    label_supprimer_identifiant_caissier_manager.grid(row = 1, column = 0, sticky = W, padx = 35, pady = 10)
    zone_de_saisi_supprimer_identifiant_caissier_manager = Entry(interface_pour_supprimer_un_caissier_et_un_manager, font = ("Arial", 12), bg = '#e3e3e3', bd = 3, width = 27)
    zone_de_saisi_supprimer_identifiant_caissier_manager.grid(row = 1, column = 1, sticky = E, padx = 35, pady = 10)
    zone_de_saisi_supprimer_identifiant_caissier_manager.focus()


    wb = load_workbook('base_de_données_caissiers_et_managers.xlsx')
    sheet = wb.active
    data = pd.read_excel('base_de_données_caissiers_et_managers.xlsx')

    def mess():
        mask = data["Identifiant"].values
        if zone_de_saisi_supprimer_identifiant_caissier_manager.get() in mask:
            zone_de_saisi_supprimer_identifiant_caissier_manager.delete(0, END)
            supprime_avec_succes()
        else:
            zone_de_saisi_supprimer_identifiant_caissier_manager.delete(0, END)
            identifiant_incorrect()

    def remove(sheet, row):
        for cell in row:
            if cell.value != zone_de_saisi_supprimer_identifiant_caissier_manager.get():
                return
            else:
                sheet.delete_rows(row[0].row, 1)
            

    def supprimer():
        for row in sheet:
            remove(sheet, row)
        wb.save('base_de_données_caissiers_et_managers.xlsx')
        mess()


    def vider():
        zone_de_saisi_supprimer_identifiant_caissier_manager.delete(0, END)


    def quitter():
        interface_pour_supprimer_un_caissier_et_un_manager.destroy()


    bouton_pour_supprimer = Button(interface_pour_supprimer_un_caissier_et_un_manager, text = "Supprimer", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = 'red', activebackground = 'red', activeforeground = 'white', cursor = 'hand2', command = supprimer)
    bouton_pour_supprimer.grid(row = 2, column = 1, sticky = E, padx = 35, pady = 30)


    bouton_pour_quitter = Button(interface_pour_supprimer_un_caissier_et_un_manager, text = "Vider", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#F4D03F', activebackground = '#F4D03F', activeforeground = 'white', cursor = 'hand2', command = vider)
    bouton_pour_quitter.grid(row = 2, columnspan = 2)


    bouton_pour_quitter = Button(interface_pour_supprimer_un_caissier_et_un_manager, text = "Quitter", font = ('Arial', 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#F32665', activebackground = '#F32665', activeforeground = 'white', cursor = 'hand2', command = quitter)
    bouton_pour_quitter.grid(row = 2, column = 0, sticky = W, padx = 35, pady = 30)

#interface_pour_supprimer_un_caissier_et_un_manager.mainloop()