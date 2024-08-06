from flask import Blueprint
from db.mongo import mongo_instance, get_projects , add_project


projects = Blueprint('projects', __name__)

@projects.route('/zeca')
def index():
  return get_projects()

@projects.route('/zecao')
def indexx():
  return add_project()