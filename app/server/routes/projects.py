import json
import logging
from flask import Blueprint, request, jsonify, Response
import datetime

from decorators import login_required
from models.Projects import Projects


projects_service = Projects()


projects = Blueprint('projects', __name__)

@projects.route('/api/projects', methods=['GET'])
def get_projects_route():
  projects_list = projects_service.get_projects()
  return Response(projects_list, mimetype='application/json')

@projects.route('/api/project/<project_id>', methods=['GET'])
def get_project_route(project_id):
  if not project_id:
    return jsonify({"error":"project not defined"}), 400

  project = projects_service.get_project_by_id(project_id)
  logging.info(project)
  return Response(project, mimetype='application/json')

@projects.route('/api/add-project', methods=['POST'])
@login_required
def set_project():
  try:
    project = request.get_json()
    projects_service.add_project(project)
    return Response(response="Created", status=201)
  except Exception as error:
    logging.error(error)
    return Response(response="Error", status=400)

@projects.route('/api/edit-project/<project_id>', methods=['PUT'])
@login_required
def edit_project(project_id):
  return project_id

@projects.route('/api/delete-project/<project_id>', methods=['DELETE'])
@login_required
def delete_project(project_id):
  try:
    projects_service.delete_project(project_id)
    return Response(response="Done", status=200)
  except Exception as error:
    logging.error(error)
    return Response(response="Error", status=400)
