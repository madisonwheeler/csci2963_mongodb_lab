from pymongo import MongoClient
import bson
from bson.objectid import ObjectId

client = MongoClient()
db = client.csci2963
defs = db.definitions

print "All records"
for post in defs.find():
  print post

print "\nOne record"
doc = defs.find_one()
print doc

print "\nSpecific record"
doc = defs.find_one({"word": "Capitaland"})
print doc

print "\nSpecific ID"
def get(post_id):
  document = defs.find_one({'_id': ObjectId(post_id)})
  return document

doc = get("56fe9e22bad6b23cde07b8ce")
print doc

print "\nInsert"
post_id = defs.insert_one({"word": "Flugelhorn", "definition": "instrument"})
print post_id
