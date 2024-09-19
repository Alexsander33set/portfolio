from flask import request, jsonify
import jwt

from models.Users import User

# Chave secreta para assinar os tokens
SECRET_KEY = 'your_secret_key'

# Função para verificar o token JWT
def token_required(f):
    def decorated(*args, **kwargs):
        token = None
        # Verifica se o token está no header da requisição
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            # Decodifica o token usando a chave secreta
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = data['user_id']
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated
  
def create_token(user: User):
  payload = {
    'user_id': user.email,
  }
  return jwt.encode(payload, SECRET_KEY, algorithm="HS256").decode('utf-8')