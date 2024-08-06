import os
import pymongo
from flask import jsonify
import logging
import pprint

MONGO_URL = os.getenv("MONGO_URL")
mongo_instance = pymongo.MongoClient(MONGO_URL)

db = mongo_instance["portfolio"]
collection = db['projects']

example = {
  "name": "Weather Forecast",
  "slug": "weather-forecast",
  "description": "something",
  "technologies": [],
  "url": "www.apfs.com.br"
}

import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


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
    logging.info(" >>=====  Get Projects called =====<<")
    response= []
    try:
      for i in collection.find():
        pprint.pprint(i)
        response.append(i)
    except:
      print("error on get projects")
      
    return JSONEncoder().encode(response)
  
def get_project_by_slug(slug):
  print("")

def set_project_priority():
  print("")
  
def add_project():
  result = collection.insert_one(example)
  return str(result)
  
def remove_project():
  print("")