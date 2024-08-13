import datetime

from flask import Blueprint
from db.mongo import get_projects, add_project





projects = Blueprint('projects', __name__)

@projects.route('/api/projects')
def get_projects_route():
  return get_projects()

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