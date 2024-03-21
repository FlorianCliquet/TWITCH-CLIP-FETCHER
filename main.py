import tkinter as tk
from tkinter import messagebox
from threading import Thread
from Scripts.RecupClipURL import RecupClipURL
from Scripts.DownloadClip import DownloadClip
from Scripts.MontageClip import MontageClip
from Scripts.upload import upload

def run_program():
    category = variable.get()
    if category:
        processing_label.config(text="Traitement en cours...")
        run_button.config(state="disabled")
        quit_button.config(state="disabled")

        def execute_programs():
            RecupClipURL(category)
            DownloadClip(category)
            MontageClip(category)
            #upload(category)

            root.destroy()  # Ferme la fenêtre une fois terminé

        thread = Thread(target=execute_programs)
        thread.start()
    else:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner une catégorie.")

def quit_app():
    root.destroy()

root = tk.Tk()
root.title("Application de Téléchargement de Clips")

categories = [
    "league-of-legends",
    "fortnite",
    "valorant",
    "Autre"
]

variable = tk.StringVar(root)
variable.set(categories[0])

label = tk.Label(root, text="Sélectionnez une catégorie :")
label.pack()

option_menu = tk.OptionMenu(root, variable, *categories)
option_menu.pack()

processing_label = tk.Label(root, text="")
processing_label.pack()

run_button = tk.Button(root, text="Exécuter", command=run_program)
run_button.pack()

quit_button = tk.Button(root, text="Quitter", command=quit_app)
quit_button.pack()

root.mainloop()
