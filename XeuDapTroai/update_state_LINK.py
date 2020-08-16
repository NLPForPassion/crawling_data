from pymongo import MongoClient

client = MongoClient("mongodb+srv://17102591:Hao0215817@cluster0.bufis.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.NLP
db.LINK.update_many({},{ "$set": { "state": "Yes" } })
