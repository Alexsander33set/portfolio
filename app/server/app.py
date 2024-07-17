import os
from flask import Flask, jsonify, send_from_directory
from gevent.pywsgi import WSGIServer

from utils.toml_tools import parse_toml_file

#* ==============================================
PORT = int(os.getenv('PORT', default=8080))

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('./template', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('./template', path)


@app.route('/api/projects')
def get_projects(): 
    projects = parse_toml_file('projects.toml', 'projects')
    if not projects:
        return 404
    print(projects)
    return jsonify(projects), 200 

if __name__ == '__main__':
    print(f"\nrunning at: localhost:{PORT}\n")
    # app.run(debug=False)
    http_server = WSGIServer(('0.0.0.0', PORT), app)
    http_server.serve_forever()