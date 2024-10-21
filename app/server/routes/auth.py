import logging

from flask import Blueprint, redirect, url_for, session, request
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from google.auth.transport import requests
import os

auth = Blueprint('auth', __name__)

# OAuth Flow
flow = Flow.from_client_config(
    {
        "web": {
            "client_id": os.getenv("GOOGLE_CLIENT_ID"),
            "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "redirect_uri": os.getenv("GOOGLE_REDIRECT_URI")
        }
    },
    scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email',
            'https://www.googleapis.com/auth/userinfo.profile']
)


@auth.route("/login")
def login():
    flow.redirect_uri = os.getenv("GOOGLE_REDIRECT_URI")
    authorization_url, state = flow.authorization_url()
    session['state'] = state
    return redirect(authorization_url)


@auth.route("/callback")
def callback():
    # Get the authentication token response
    flow.fetch_token(authorization_response=request.url)

    if not session['state'] == request.args['state']:
        return "State does not match!", 400

    credentials = flow.credentials
    request_session = requests.Request()

    # Checks token ID and get authentication user info
    id_info = id_token.verify_oauth2_token(
        id_token=credentials.id_token,
        request=request_session,
        audience=os.getenv("GOOGLE_CLIENT_ID")
    )
    #* Store Google ID and User email
    session['google_id'] = id_info.get('sub')
    session['email'] = id_info.get('email')

    return redirect(url_for('client.index'))


@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('client.index'))
