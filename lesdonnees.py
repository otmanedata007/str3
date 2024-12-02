import streamlit as st
from streamlit_option_menu import option_menu

# Configuration du menu principal
selection = option_menu(
    menu_title=None,  # Aucun titre pour le menu
    options=["Accueil", "Photos", "À propos"],  # Options du menu
    icons=["house", "camera", "info-circle"],  # Icônes pour chaque option
    menu_icon="cast",  # Icône du menu
    default_index=0,  # Option par défaut
    orientation="horizontal",  # Menu affiché horizontalement
)

# Affichage du contenu selon l'option sélectionnée
if selection == "Accueil":
    st.title("Bienvenue sur la page d'accueil !")
    st.write("Ceci est la section principale de votre application.")

elif selection == "Photos":
    st.title("Bienvenue sur l'album photo")
    st.write("Explorez toutes vos photos ici.")
    st.image(
        "https://via.placeholder.com/400x300", 
        caption="Photo exemple",
        width=400
    )

elif selection == "À propos":
    st.title("À propos de cette application")
    st.write("""
        Cette application est un exemple utilisant Streamlit Option Menu.
        Elle permet de naviguer facilement entre différentes sections.
    """)
    st.info("Contactez-nous pour plus d'informations.")

# Ajoutez ici d'autres pages ou sections si nécessaire.
