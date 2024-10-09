import logging

from flask import json
from models.Mongo import MongoDB

class Projects(MongoDB):
    def __init__(self):
        # Connects to the "mydatabase" database and "projects" collection
        super().__init__(collection_name="projects")

    def get_projects(self):
        logging.debug(" >>=====  Get projects called =====<<")
        projects = self.find_all()
        
        for project in projects:
            project['_id'] = str(project['_id'])  # Convert ObjectId to string
        return json.dumps(projects)

    def get_project(self, slug):
        logging.info(" >>=====  Get Project called =====<<")
        return self.find_one({'slug': slug})

    def add_project(self, project_data):
        """Adds a new project"""
        return self.insert_one(project_data)

    def update_project(self, project_id, updated_data):
        """Updates a project by ID"""
        logging.info(" >>=====  Update project called =====<<")
        query = {'_id': project_id}
        return self.update_one(query, updated_data)

    def delete_project(self, project_id):
        """Removes a project by ID"""
        logging.info(" >>=====  Remove project called =====<<")
        query = {'_id': project_id}
        return self.delete_one(query)
    
    def set_project_priority(self, slug, new_priority):
        logging.info(" >>=====  Set project priority called =====<<")
        return self.update_one({"slug": slug}, {"$set": {"priority": new_priority}})









#class Projects:
#
#  def get_projects():
#    logging.info(" >>=====  Get projects called =====<<")
#    projects = list(projects_collection.find())
#    for project in projects:
#        project['_id'] = str(project['_id'])  # Converter ObjectId para string
#    return json.dumps(projects)
#  
#  def get_project(slug:str):
#    logging.info(" >>=====  Get Project called =====<<")
#      project = projects_collection.find_one({"slug": slug})
#      if project:
#        project['_id'] = str(project['_id'])  # Converter ObjectId para string
#    return json.dumps(project)
#
#  def set_project_priority(slug, new_priority):
#    logging.info(" >>=====  Set project priority called =====<<")
#    return projects_collection.update_one({"slug": slug}, {"$set": {"priority": new_priority}})
#
#  def add_project(project):
#    logging.info(" >>=====  Add project called =====<<")
#    return projects_collection.insert_one(project)
#
#  def remove_project(slug):
#      logging.info(" >>=====  Remove project called =====<<")
#      return projects_collection.delete_one({"slug": slug})