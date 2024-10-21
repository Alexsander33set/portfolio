import os
from flask import Flask
#*
import logging

from decorators import login_required

logging.getLogger().setLevel(logging.INFO)
#*
from dotenv import load_dotenv
load_dotenv()

#* ==============================================
from routes.client import client
from routes.projects import projects
from routes.auth import auth
from utils.jwt import token_required

PORT = int(os.getenv('PORT', default=80))
app = Flask(__name__)

#* == Blueprints =============================================
app.register_blueprint(client)
app.register_blueprint(projects)
app.register_blueprint(auth, url_prefix='/auth')

@app.route('/admin', methods=['GET'])
@login_required
def admin():
    return 'Admin'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=PORT, debug='True')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
