import pymongo

client = pymongo.MongoClient("mongodb+srv://atharv:atharvs95@alphatron.7zud5uc.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"atharv",
    "email": "atharvdixit95@gmail.com",
    "surname": "dixit"
}

db1= client['mongotest1']
coll= db1['test']
coll.insert_one(d)
