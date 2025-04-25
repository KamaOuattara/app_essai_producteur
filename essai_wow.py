import tkinter as tk
from tkinter import messagebox, scrolledtext

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interface Producteur Agricole")
        self.geometry("600x450")
        self._create_widgets()

    def _create_widgets(self):
        # Frame de saisie
        frame_input = tk.LabelFrame(self, text="Saisie des informations", padx=10, pady=10)
        frame_input.pack(padx=10, pady=10, fill='x')

        # Nom du producteur
        tk.Label(frame_input, text="Nom du producteur:").grid(row=0, column=0, sticky='w')
        self.entry_nom = tk.Entry(frame_input)
        self.entry_nom.grid(row=0, column=1, sticky='ew', pady=2)

        # Spéculation
        tk.Label(frame_input, text="Spéculation:").grid(row=1, column=0, sticky='w')
        self.entry_spec = tk.Entry(frame_input)
        self.entry_spec.grid(row=1, column=1, sticky='ew', pady=2)

        # Superficie
        tk.Label(frame_input, text="Superficie (ha):").grid(row=2, column=0, sticky='w')
        self.entry_sup = tk.Entry(frame_input)
        self.entry_sup.grid(row=2, column=1, sticky='ew', pady=2)

        # Production
        tk.Label(frame_input, text="Production (kg):").grid(row=3, column=0, sticky='w')
        self.entry_prod = tk.Entry(frame_input)
        self.entry_prod.grid(row=3, column=1, sticky='ew', pady=2)

        # Configuration de la grille
        frame_input.columnconfigure(1, weight=1)

        # Bouton Valider
        btn_valider = tk.Button(self, text="Valider", command=self._on_validate)
        btn_valider.pack(pady=5)

        # Zone de résultat
        frame_output = tk.LabelFrame(self, text="Résultat", padx=10, pady=10)
        frame_output.pack(padx=10, pady=10, fill='both', expand=True)
        self.text_output = scrolledtext.ScrolledText(frame_output, wrap='word')
        self.text_output.pack(fill='both', expand=True)

    def _on_validate(self):
        nom = self.entry_nom.get().strip()
        spec = self.entry_spec.get().strip()
        sup = self.entry_sup.get().strip()
        prod = self.entry_prod.get().strip()

        # Validation des entrées
        if not nom.isalpha():
            messagebox.showerror("Erreur", "Entrez des lettres pour le nom du producteur.")
            return
        if not spec.isalpha():
            messagebox.showerror("Erreur", "Entrez des lettres pour la spéculation.")
            return
        if not sup.isdigit():
            messagebox.showerror("Erreur", "Entrez un nombre pour la superficie.")
            return
        if not prod.isdigit():
            messagebox.showerror("Erreur", "Entrez un nombre pour la production.")
            return

        # Calculs et affichage
        prix_kg = 438
        certification = True
        message = (
            f"Bonjour 🫡 {nom}, vous avez un champ de {spec} d'une superficie de {sup} ha, "
            f"dont la production est de {prod} kg, qui coûte {prix_kg} FCFA/kg. "
            f"Certification : {'Oui' if certification else 'Non'}."
        )
        self._display_result(message)

    def _display_result(self, text):
        self.text_output.delete('1.0', tk.END)
        self.text_output.insert(tk.END, text)

if __name__ == "__main__":
    app = App()
    app.mainloop()
