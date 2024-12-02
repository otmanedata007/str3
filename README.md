# str3
# Streamlit Authenticator
import streamlit as st
from streamlit_authenticator import Authenticate

# Définir les données des comptes utilisateurs
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'Utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attempts': 0,  # Géré automatiquement
            'logged_in': False,  # Géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'Administrateur',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attempts': 0,  # Géré automatiquement
            'logged_in': False,  # Géré automatiquement
            'role': 'administrateur'
        }
    }
}

# Créer une instance d'authentification
authenticator = Authenticate(
    credentials=lesDonneesDesComptes,  # Données des comptes utilisateurs
    cookie_name="auth_cookie",         # Nom du cookie
    key="auth_key",                    # Clé de cookie
    cookie_expiry_days=30              # Expiration du cookie
)

# Afficher le formulaire de connexion
authenticator.login()

# Définir une fonction pour afficher le contenu protégé
def accueil():
    st.title("Bienvenue sur votre application Streamlit sécurisée!")
    st.write("Vous êtes maintenant connecté(e).")

# Gérer les états d'authentification
if st.session_state["authentication_status"]:
    accueil()
    authenticator.logout("Se déconnecter")
elif st.session_state["authentication_status"] is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect.")
elif st.session_state["authentication_status"] is None:
    st.warning("Veuillez entrer vos identifiants pour vous connecter.")
