from pymongo import MongoClient
client = MongoClient('mongodb+srv://Muhammadzhafar437:Makannasi437@cluster0.dkiemu6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta
doc = {
    'name':'bob',
    'age':27
}

db.users.insert_one(doc)