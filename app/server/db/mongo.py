import os, logging, json, datetime, pprint, pymongo

from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
  def default(self, o):
    if isinstance(o, ObjectId):
      return str(o)
    # if isinstance(o, (datetime, datetime.date)):
    #   return o.isoformat()
    return json.JSONEncoder.default(self, o)


MONGO_URL = os.getenv("MONGO_URL")
if not MONGO_URL:
  print("MONGO_URL not defined")

db = pymongo.MongoClient(MONGO_URL)["portfolio"]
projects_collection = db['projects']

example = {
  "name": "Weather Forecast",
  "slug": "weather-forecast",
  "description": "something",
  "technologies": ["java","node","python"],
  "url": "www.apfs.com.br",
  "is_private": False,
  "created_at": datetime.datetime.now()
}


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
      for i in projects_collection.find():
        pprint.pprint(i)
        response.append(i)
    except:
      print("error on get projects")
    
    # TODO: fix response with created_at
    return JSONEncoder().encode(response)
  
def get_project_by_slug(slug):
  try:
    response = projects_collection.find_one({"slug": slug})
  except:
    response = "something isn't right...."
  return JSONEncoder().encode(response)

def set_project_priority():
  print("")
  
def add_project():
  result = ""
  try:
    result = projects_collection.insert_one(example)
  except:
    result = "erro"
  return str(result)
  
def remove_project():
  print("")