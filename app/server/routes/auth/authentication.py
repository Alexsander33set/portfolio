from flask import Blueprint, redirect, request, jsonify

from utils.jwt import create_token
from models.Users import User

#* add google oauth

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
  email, password = request.params
  user = User(email, password)
  user.validate() #* if user is valid, create a token and return it
  token = create_token(user)
  return jsonify({'token': token})

@auth.route('/logout')
def logout():
    #* TODO: add logout logic
    redirect('/')
    
@auth.route('/token-validation')
def token_validation():
  token = request.params['token']
  #* TODO: add token validation logic
  return jsonify({'valid': True})


