from flask import Blueprint, send_from_directory

client = Blueprint('client', __name__)

@client.route('/')
def index():
    return send_from_directory('./template', 'index.html')

@client.route('/<path:path>')
def serve_static(path):
    return send_from_directory('./template', path)