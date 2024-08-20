from redis_integration.db import get_db

r = get_db()

def add_recipe(recipe_id, name, description, ingredients, steps):
    r.hset(f"recipe:{recipe_id}", mapping={
        "name": name,
        "description": description,
        "ingredients": ingredients,
        "steps": steps
    })

def get_recipe(recipe_id):
    return r.hgetall(f"recipe:{recipe_id}")
