import os
from flask import Flask
#*
import logging
logging.getLogger().setLevel(logging.INFO)
#*
from dotenv import load_dotenv
load_dotenv()

#* ==============================================
from routes.client import client
from routes.projects import projects
from routes.auth.authentication import auth
from utils.jwt import token_required

PORT = int(os.getenv('PORT', default=8080))
app = Flask(__name__)

#* == Blueprints =============================================
app.register_blueprint(client)
app.register_blueprint(projects)
app.register_blueprint(auth, url_prefix='/auth')

@app.route('/admin', methods=['GET'])
@token_required
def admin():
    return 'Admin'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=PORT, debug='True')
