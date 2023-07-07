from pymongo import MongoClient

# Establish a connection to MongoDB
client = MongoClient('mongodb://localhost:27017')

# Access the database and collection
db = client['telegrambot']
collection = db['c_datas']

# Define the query filter
query = {"title": "muruga"}

# Retrieve documents that match the query filter
documents = collection.find(query)

# Process the retrieved documents
for doc in documents:
    print(doc)

# Close the connection
client.close()
