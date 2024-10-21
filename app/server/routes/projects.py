import json
import logging
from flask import Blueprint, request, jsonify, Response
import datetime

from decorators import login_required
from models.Projects import Projects


projects_service = Projects()


projects = Blueprint('projects', __name__)

@projects.route('/api/projects')
def get_projects_route():
  projects = projects_service.get_projects()
  return Response(projects, mimetype='application/json')

@projects.route('/api/project/<slug>')
def get_project_route(slug):
  if not slug:
    return jsonify({"error":"project not defined"}), 400
  
  logging.info(slug)
  
  project = projects_service.get_project(slug)
  return Response(project, mimetype='application/json')

@projects.route('/api/add-project')
@login_required
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


  return projects_service.add_project(example)