from flask import Blueprint, send_from_directory

from decorators import login_required

client = Blueprint('client', __name__)

@client.route('/')
def index():
    return send_from_directory('./template', 'index.html')

@client.route('/<path:path>')
def serve_static(path):
    return send_from_directory('./template', path)

@client.route('/admin', methods=['GET'])
@login_required
def admin():
    return send_from_directory('./template', 'index.html')