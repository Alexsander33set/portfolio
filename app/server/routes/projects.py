from flask import Blueprint
from db.mongo import get_projects, add_project


projects = Blueprint('projects', __name__)

@projects.route('/api/projects')
def get_projects_route():
  return get_projects()

@projects.route('/api/add-project')
def set_project():
  return add_project()