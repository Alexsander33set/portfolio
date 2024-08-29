import datetime

from flask import Blueprint, request, jsonify, Response
from db.mongo import get_projects, add_project, get_project





projects = Blueprint('projects', __name__)

@projects.route('/api/projects')
def get_projects_route():
  projects = get_projects()
  return Response(projects, mimetype='application/json')

@projects.route('/api/project/<slug>')
def get_project_route(slug):
  if not slug:
    return jsonify({"error":"project not defined"}), 400
  
  project = get_project(slug)
  return Response(project, mimetype='application/json')

@projects.route('/api/add-project')
def set_project():
  example = {
    "name": "Weather Forecast",
    "slug": "weather-forecast",
    "description": "something",
    "technologies": ["java", "node", "python"],
    "url": "www.apfs.com.br",
    "is_private": False,
    "created_at": int(datetime.datetime.now().timestamp())
  }


  return add_project(example)