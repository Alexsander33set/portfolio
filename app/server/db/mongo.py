import json
import logging
import os

import pymongo

from bson import ObjectId
class JSONEncoder(json.JSONEncoder):
  def default(self, o):
    if isinstance(o, ObjectId):
      return str(o)
    return json.JSONEncoder.default(self, o)
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
#* ping_route
#* is_private
#* created_at
#*


def get_projects():
    logging.info(" >>=====  Get projects called =====<<")
    response= []
    try:
      for i in projects_collection.find():
        response.append(i)
    except:
      print("error on get projects")

    return JSONEncoder().encode(response)

def get_project(slug:str):
  logging.info(" >>=====  Get Project called =====<<")
  try:
    response = projects_collection.find_one({"slug": slug})
  except:
    response = "something isn't right...."
  return JSONEncoder().encode(response)

def set_project_priority(slug, new_priority):
  logging.info(" >>=====  Set project priority called =====<<")
  print("")

def add_project(project):
  logging.info(" >>=====  Add project called =====<<")
  result = ""
  try:
    result = projects_collection.insert_one(project)
  except:
    result = "erro"
  return str(result)

def remove_project():
  logging.info(" >>=====  Remove project called =====<<")
  print("")