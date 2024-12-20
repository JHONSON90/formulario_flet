import pyrebase
import os
import firebase_admin
import pickle
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials


cred = credentials.Certificate("G:/EDISON/computador/VARIOS EDISON/PROHIBIDO NO TOCAR/CursoPrepHenry/flet/aplicacion_formulario/service_account.json")
firebase_admin.initialize_app(cred)

firebaseConfig = {
  "apiKey": "AIzaSyAVBEGF8tyoOenFpszB1DVkvqPmkwrhli4",
  "authDomain": "registro-usuarios-98f91.firebaseapp.com",
  "projectId": "registro-usuarios-98f91",
  "storageBucket": "registro-usuarios-98f91.firebasestorage.app",
  "messagingSenderId": "974951175878",
  "appId": "1:974951175878:web:16517dbba56ca53899a9c7",
  "measurementId": "G-MGCQM3L90S",
  "databaseURL":"https://registro-usuarios-98f91-default-rtdb.firebaseio.com/"
  
};

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def create_user(name, email, password):
    try:
        user = firebase_auth.create_user(
            email=email,
            password=password,
            display_name=name)
        return user.uid
    except:
        return None


def reset_password(email):
    try:
        firebase_auth.generate_password_reset_link(email)
        print(f"recibo del frontend este email {email}")
        return {"success":True} # cambio el not None por True
    except Exception as e: 
        return {"success": False, "message": f"Ocurrió un error al restablecer la contraseña. {e}"} #cambiamos el None por un manejo de errores


def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user['idToken']
    except:
        return None


def store_session(token):
    if os.path.exists('token.pickle'):
        os.remove('token.pickle')
    with open('token.pickle', 'wb') as f:
        pickle.dump(token, f)


def load_token():
    try:
        with open('token.pickle', 'rb') as f:
            token = pickle.load(f)
        return token
    except Exception as e:
            print(f"este es el error al cargar el token {e}")
            return None


def authenticate_token(token):
    try:
        result = firebase_auth.verify_id_token(token)
        return result['user_id']
    except:
        return None


def get_name(token):
    try:
        result = firebase_auth.verify_id_token(token)
        return result['name']
    except:
        return None


def revoke_token(token):
    result = firebase_auth.revoke_refresh_tokens(authenticate_token(token))
    if os.path.exists('token.pickle'):
        os.remove('token.pickle')


# email = "edisonportillal@gmail.com"
# password = "1085917679JHon@"

# token = login_user(email, password)
# print(f"store {store_session(token)}")
# print(f"cargo el token{load_token()}")
# print(f"autentico el token{authenticate_token(token)}")
# print(f"tengo el nombre del cliente {get_name(token)}")