from pymongo import MongoClient

# Replace this URI with your MongoDB connection string
client = MongoClient("mongodb+srv://asrushfig:2003@cluster0.6vdid.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ludo_game"]
collection = db["games"]

def save_game(chat_id, data):
    collection.update_one({"chat_id": chat_id}, {"$set": data}, upsert=True)

def load_game(chat_id):
    return collection.find_one({"chat_id": chat_id})

def delete_game(chat_id):
    collection.delete_one({"chat_id": chat_id})
