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
#auth = firebase_admin.auth()

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
        firebase_auth.send_password_reset_email(email)
        return not None
    except:
        return None


def login_user(email, password):
    try:
        user = firebase_auth.sign_in_with_email_and_password(email, password)
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
    except:
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
