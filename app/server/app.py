from flask import Flask, jsonify, send_from_directory

from utils.toml_tools import parse_toml_file

# ==============================================


app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('./template', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('./template', path)


@app.route('/api/projects')
def get_projects():
    
    try:
        projects = parse_toml_file('projects.toml')
        return jsonify(projects)
    except:
        return jsonify({"error":"500"})
    