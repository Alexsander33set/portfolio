import os
from flask import Flask, send_from_directory
#*
import logging
logging.getLogger().setLevel(logging.INFO)
#*
from dotenv import load_dotenv
load_dotenv()

#* ==============================================
from routes.projects import projects


PORT = int(os.getenv('PORT', default=8080))
app = Flask(__name__)

#* == Blueprints =============================================
app.register_blueprint(projects)


@app.route('/')
def index():
    return send_from_directory('./template', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('./template', path)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=PORT, debug='True')
