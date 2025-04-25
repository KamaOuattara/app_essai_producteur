import streamlit as st

st.title("Interface Producteur Agricole")

# Création d'un formulaire pour regrouper les champs
with st.form(key="producer_form"):
    nom       = st.text_input("Nom du producteur")               # champ texte :contentReference[oaicite:6]{index=6}
    spec      = st.text_input("Spéculation")                     # champ texte :contentReference[oaicite:7]{index=7}
    sup       = st.text_input("Superficie (ha)")                 # champ numérique en mode texte :contentReference[oaicite:8]{index=8}
    prod      = st.text_input("Production (kg)")                 # champ numérique en mode texte :contentReference[oaicite:9]{index=9}

    # Bouton de soumission unique pour tout le formulaire
    submit_btn = st.form_submit_button(label="Valider")          # bouton de formulaire :contentReference[oaicite:10]{index=10}

# Traitement après soumission
if submit_btn:
    # Validation basique
    if not (nom.isalpha() and spec.isalpha() and sup.isdigit() and prod.isdigit()):
        st.error("Veuillez remplir correctement tous les champs (lettres ou chiffres uniquement).")  
    else:
        prix_kg       = 438
        certification = True
        # Calcul du message
        message = (
            f"Bonjour 🫡 {nom}, vous avez un champ de {spec} "
            f"d'une superficie de {sup} ha, dont la production est de {prod} kg, "
            f"qui coûte {prix_kg} FCFA/kg. Certification : {'Oui' if certification else 'Non'}."
        )
        st.success(message)                                      # affichage dynamique :contentReference[oaicite:11]{index=11}