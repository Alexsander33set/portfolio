import json
import logging
import os

import pymongo

#* =====================================================

MONGO_URL :str|None = os.getenv("MONGO_URL")
if not MONGO_URL:
  raise AttributeError("MONGO_URL not defined")

db = pymongo.MongoClient(MONGO_URL)["portfolio"]
projects_collection = db['projects']


#* project
#*
#* name
#* slug
#* description
#* technologies
#* url
#* priority
#* is_private
#* created_at
#*


def get_projects():
    logging.info(" >>=====  Get projects called =====<<")
    projects = list(projects_collection.find())
    for project in projects:
        project['_id'] = str(project['_id'])  # Converter ObjectId para string
    return json.dumps(projects)
  
def get_project(slug:str):
  logging.info(" >>=====  Get Project called =====<<")
  project = projects_collection.find_one({"slug": slug})
  if project:
      project['_id'] = str(project['_id'])  # Converter ObjectId para string
  return json.dumps(project)

def set_project_priority(slug, new_priority):
  logging.info(" >>=====  Set project priority called =====<<")
  print("")

def add_project(project):
  logging.info(" >>=====  Add project called =====<<")
  result = ""
  return projects_collection.insert_one(project)

def remove_project():
  logging.info(" >>=====  Remove project called =====<<")
  print("")