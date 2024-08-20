from pymongo import MongoClient
from redis_integration.models import add_recipe

def migrate_data():
    # Conectar a MongoDB
    mongo_client = MongoClient("mongodb://localhost:27017/")
    mongo_db = mongo_client["recetario"]
    mongo_collection = mongo_db["recetas"]

    # Migrar datos a Redis
    for recipe in mongo_collection.find():
        add_recipe(recipe["_id"], recipe["name"], recipe["description"], recipe["ingredients"], recipe["steps"])

if __name__ == "__main__":
    migrate_data()
