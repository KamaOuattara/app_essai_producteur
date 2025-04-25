import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interface Producteur Agricole Interactive")
        self.configure(bg="#f0f4f7")
        self.geometry("700x450")
        self._create_styles()
        self._create_widgets()

    def _create_styles(self):
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('TLabel', background='#f0f4f7', font=('Arial', 11))
        style.configure('TButton', background='#4caf50', foreground='white', font=('Arial', 11), padding=6)
        style.map('TButton', background=[('active', '#45a049')])
        style.configure('TLabelframe', background='#e1ebee', font=('Arial', 12, 'bold'))
        style.configure('TLabelframe.Label', background='#e1ebee')

    def _create_widgets(self):
        # Variables liées aux champs pour mise à jour dynamique
        self.nom_var = tk.StringVar()
        self.spec_var = tk.StringVar()
        self.sup_var = tk.StringVar()
        self.prod_var = tk.StringVar()

        # Frame de saisie
        frame_input = ttk.Labelframe(self, text="Saisie des informations")
        frame_input.place(x=20, y=20, width=660, height=180)

        labels = ['Nom du producteur:', 'Spéculation:', 'Superficie (ha):', 'Production (kg):']
        vars_list = [self.nom_var, self.spec_var, self.sup_var, self.prod_var]
        entries = []
        for i, (text, var) in enumerate(zip(labels, vars_list)):
            lbl = ttk.Label(frame_input, text=text)
            lbl.grid(row=i, column=0, sticky='w', padx=10, pady=5)
            ent = ttk.Entry(frame_input, textvariable=var)
            ent.grid(row=i, column=1, sticky='ew', padx=10, pady=5)
            entries.append(ent)
            # Liaison dynamique
            var.trace_add('write', self._update_preview)

        self.entry_widgets = entries
        frame_input.columnconfigure(1, weight=1)

        # Zone de résultat interactive
        frame_output = ttk.Labelframe(self, text="Aperçu en temps réel")
        frame_output.place(x=20, y=220, width=660, height=200)
        self.text_output = scrolledtext.ScrolledText(frame_output, wrap='word', height=8)
        self.text_output.pack(fill='both', expand=True, padx=10, pady=5)

        # Bouton pour effacer
        btn_clear = ttk.Button(self, text="Effacer", command=self._clear_all)
        btn_clear.place(x=300, y=430)

        # Initialisation du preview
        self._update_preview()

    def _update_preview(self, *args):
        nom = self.nom_var.get().strip()
        spec = self.spec_var.get().strip()
        sup = self.sup_var.get().strip()
        prod = self.prod_var.get().strip()

        # Construction du message d'aperçu
        prix_kg = 438
        certification = True
        if all([nom.isalpha(), spec.isalpha(), sup.isdigit(), prod.isdigit()]):
            message = (
                f"Bonjour 🫡 {nom}, vous avez un champ de {spec} d'une superficie de {sup} ha, "
                f"dont la production est de {prod} kg, qui coûte {prix_kg} FCFA/kg. "
                f"Certification : {'Oui' if certification else 'Non'}."
            )
        else:
            message = "Remplissez tous les champs correctement pour voir l'aperçu."

        # Affichage
        self.text_output.delete('1.0', tk.END)
        self.text_output.insert(tk.END, message)

    def _clear_all(self):
        # Réinitialise les champs
        for var in [self.nom_var, self.spec_var, self.sup_var, self.prod_var]:
            var.set("")
        self.text_output.delete('1.0', tk.END)

if __name__ == "__main__":
    app = App()
    app.mainloop()