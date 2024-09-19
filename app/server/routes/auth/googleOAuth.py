from flask import Blueprint, redirect, url_for, session, request
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

auth_bp = Blueprint('auth', __name__)

class GoogleOAuth:
    def __init__(self):
        self.client_secrets_file = "client_secret.json"
        self.scopes = ["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email"]
        self.flow = Flow.from_client_secrets_file(
            self.client_secrets_file,
            scopes=self.scopes,
            redirect_uri="http://localhost:5000/auth/callback"
        )

    def get_authorization_url(self):
        authorization_url, _ = self.flow.authorization_url(prompt="consent")
        return authorization_url

    def get_user_info(self, credentials):
        service = build('oauth2', 'v2', credentials=credentials)
        user_info = service.userinfo().get().execute()
        return user_info

google_oauth = GoogleOAuth()

@auth_bp.route('/login')
def login():
    return redirect(google_oauth.get_authorization_url())

@auth_bp.route('/callback')
def callback():
    flow = google_oauth.flow
    flow.fetch_token(authorization_response=request.url)
    credentials = flow.credentials
    user_info = google_oauth.get_user_info(credentials)
    
    session['user'] = user_info
    return redirect(url_for('admin.dashboard'))

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('main.index'))

# Adicione esta função para verificar se o usuário está autenticado
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function
