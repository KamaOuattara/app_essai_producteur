from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface Producteur Agricole - PyQt5")
        self.setFixedSize(700, 450)
        self._setup_ui()

    def _setup_ui(self):
        # Styles globaux
        self.setStyleSheet("""
            QWidget { background-color: #f0f4f7; font-family: Arial; font-size: 11pt; }
            QLineEdit { background-color: white; padding: 4px; }
            QPushButton { background-color: #4caf50; color: white; padding: 6px; border: none; }
            QPushButton:hover { background-color: #45a049; }
            QTextEdit { background-color: #fcfcfc; }
        """)

        # Layout principal
        main_layout = QtWidgets.QVBoxLayout(self)
        input_group = QtWidgets.QGroupBox("Saisie des informations")
        input_group.setStyleSheet("QGroupBox { background-color: #e1ebee; font-weight: bold; padding: 10px; }")
        form_layout = QtWidgets.QFormLayout()

        # Champs de saisie
        self.nom_edit = QtWidgets.QLineEdit()
        self.spec_edit = QtWidgets.QLineEdit()
        self.sup_edit = QtWidgets.QLineEdit()
        self.prod_edit = QtWidgets.QLineEdit()

        form_layout.addRow("Nom du producteur:", self.nom_edit)
        form_layout.addRow("Spéculation:", self.spec_edit)
        form_layout.addRow("Superficie (ha):", self.sup_edit)
        form_layout.addRow("Production (kg):", self.prod_edit)
        input_group.setLayout(form_layout)

        # Boutons
        btn_layout = QtWidgets.QHBoxLayout()
        self.validate_btn = QtWidgets.QPushButton("Valider")
        self.clear_btn = QtWidgets.QPushButton("Effacer")
        btn_layout.addWidget(self.validate_btn)
        btn_layout.addWidget(self.clear_btn)

        # Zone d'aperçu
        preview_group = QtWidgets.QGroupBox("Aperçu dynamique")
        preview_group.setStyleSheet("QGroupBox { background-color: #ffffff; padding: 10px; }")
        preview_layout = QtWidgets.QVBoxLayout()
        self.preview_text = QtWidgets.QTextEdit(readOnly=True)
        preview_layout.addWidget(self.preview_text)
        preview_group.setLayout(preview_layout)

        # Assemblage
        main_layout.addWidget(input_group)
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(preview_group)

        # Connexions
        for edit in (self.nom_edit, self.spec_edit, self.sup_edit, self.prod_edit):
            edit.textChanged.connect(self.update_preview)
        self.validate_btn.clicked.connect(self.final_validate)
        self.clear_btn.clicked.connect(self.clear_all)

        # Initial preview
        self.update_preview()

    def update_preview(self):
        nom = self.nom_edit.text().strip()
        spec = self.spec_edit.text().strip()
        sup = self.sup_edit.text().strip()
        prod = self.prod_edit.text().strip()
        prix_kg = 438
        certification = True
        if nom.isalpha() and spec.isalpha() and sup.isdigit() and prod.isdigit():
            msg = (f"Bonjour 🫡 {nom}, vous avez un champ de {spec}\n"
                   f"Superficie : {sup} ha, Production : {prod} kg\n"
                   f"Coût : {prix_kg} FCFA/kg, Certification : {'Oui' if certification else 'Non'}.")
        else:
            msg = "Remplissez correctement tous les champs pour voir l'aperçu."
        self.preview_text.setPlainText(msg)

    def final_validate(self):
        nom = self.nom_edit.text().strip()
        spec = self.spec_edit.text().strip()
        sup = self.sup_edit.text().strip()
        prod = self.prod_edit.text().strip()
        if not nom.isalpha():
            QtWidgets.QMessageBox.critical(self, "Erreur", "Nom invalide. Utilisez uniquement des lettres.")
            return
        if not spec.isalpha():
            QtWidgets.QMessageBox.critical(self, "Erreur", "Spéculation invalide. Utilisez uniquement des lettres.")
            return
        if not sup.isdigit():
            QtWidgets.QMessageBox.critical(self, "Erreur", "Superficie invalide. Utilisez uniquement des chiffres.")
            return
        if not prod.isdigit():
            QtWidgets.QMessageBox.critical(self, "Erreur", "Production invalide. Utilisez uniquement des chiffres.")
            return
        QtWidgets.QMessageBox.information(self, "Succès", "Informations enregistrées avec succès !")

    def clear_all(self):
        for edit in (self.nom_edit, self.spec_edit, self.sup_edit, self.prod_edit):
            edit.clear()
        self.update_preview()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
