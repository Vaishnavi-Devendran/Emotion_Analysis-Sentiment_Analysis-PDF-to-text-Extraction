from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def upload_to_mongodb(document):
    uri = "mongodb+srv://new:BH6kutfzX0pcoVPw@resume-data.1ueh5w9.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    collection = client.resumeData.Data
    try:
      # Insert the document into the collection
      collection.insert_one(document)

      # Close the connection
      client.close()
    except Exception as e:
      print(f'mongo upload failed : {e}')


def get_resumes(query):
  uri = "mongodb+srv://new:BH6kutfzX0pcoVPw@resume-data.1ueh5w9.mongodb.net/?retryWrites=true&w=majority"

  # Create a new client and connect to the server
  client = MongoClient(uri, server_api=ServerApi('1'))
  collection = client.resumeData.Data
  # Send a ping to confirm a successful connection
  try:
    result = collection.find(query)
  except Exception as e:
    result = 0

  return result

def find_matching_resumes(required_skills):
    # Flatten the list of required skills
    flat_skills_list = [skill for sublist in required_skills for skill in sublist]

    query = {
        "$or": [
            { "skills": { "$regex": f"{skill}", "$options": "i" } }
            for skill in flat_skills_list
        ] + [
            { "skills.name": { "$regex": f"{skill}", "$options": "i" } }
            for skill in flat_skills_list
        ]
    }

    result = get_resumes(query)

    return result