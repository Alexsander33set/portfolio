import logging

from flask import json
from models.Mongo import MongoDB

from bson.objectid import ObjectId
from bson.errors import InvalidId
from utils.storage import PublicStorageConnector

class Projects(MongoDB):
    def __init__(self):
        # Connects to the database and "projects" collection
        super().__init__(collection_name="projects")
        self.storage = PublicStorageConnector()

    def get_projects(self):
        logging.debug(" >>=====  Get projects called =====<<")
        projects = self.find_all()

        return json.dumps([self.serialize_project(project, include_details_content=False) for project in projects])

    def get_project(self, slug):
        logging.info(" >>=====  Get Project called =====<<")
        return self.find_one({'slug': slug})

    def get_project_by_id(self, project_id):
        """Retrieves a project by its ID"""
        logging.info(" >>=====  Get Project by ID called =====<<")
        try:
            project = self.find_one({'_id': ObjectId(project_id)})
        except InvalidId:
            return None

        if not project:
            return None

        return self.serialize_project(project, include_details_content=True)

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
        logging.info(f" >>=====  Remove project called for {project_id} =====<<")
        query = {'_id':  ObjectId(project_id)}
        return self.delete_one(query)

    def set_project_priority(self, slug, new_priority):
        logging.info(" >>=====  Set project priority called =====<<")
        return self.update_one({"slug": slug}, {"$set": {"priority": new_priority}})

    def serialize_project(self, project, include_details_content=False):
        serialized_project = dict(project)
        serialized_project['_id'] = str(serialized_project['_id'])

        preview_asset = self.storage.resolve_asset(self._get_asset_reference(serialized_project, 'preview'))
        if preview_asset:
            serialized_project['preview_image'] = preview_asset
            serialized_project['image'] = preview_asset['url']

        details_asset = self.storage.resolve_asset(self._get_asset_reference(serialized_project, 'details'))
        if details_asset:
            serialized_project['details'] = details_asset
            if include_details_content:
                storage_description = self.storage.read_text(details_asset)
                if storage_description:
                    serialized_project['description'] = storage_description

        return serialized_project

    @staticmethod
    def _get_asset_reference(project, asset_name):
        assets = project.get('assets')
        if isinstance(assets, dict) and assets.get(asset_name):
            return assets.get(asset_name)

        legacy_fields = {
            'preview': project.get('preview_image') or project.get('image'),
            'details': project.get('details') or project.get('description_asset'),
        }
        return legacy_fields.get(asset_name)









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
