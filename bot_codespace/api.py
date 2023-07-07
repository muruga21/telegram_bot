from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client['telegrambot']



def main():
    client = MongoClient('mongodb://localhost:27017')
    db = client['telegrambot']
    return db

def fetch(db = main()):
    collection = db['c_datas']

    query = {"title": "c_comments"}

    documents = collection.find(query)

    for doc in documents:
        print(doc)

    client.close()
    
    
fetch()
