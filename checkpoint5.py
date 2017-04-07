from pymongo import MongoClient
import pymongo
from random import randint
import datetime
client = MongoClient()


db = client.csci2963
defs = db.definitions
	
n = defs.count()
#r = randint(0,n)
r = 8

i = 0
w = ""
for word in defs.find():
    if i == r:
        w = word["word"]
        t = str(datetime.datetime.now())        
        defs.update({"word":w}, {"$push": {"dates": t}})
        break
    i+=1
print defs.find_one({"word":w})
