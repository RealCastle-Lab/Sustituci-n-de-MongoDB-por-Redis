from redis_integration.models import add_recipe, get_recipe

def create_recipe(recipe_id, name, description, ingredients, steps):
    add_recipe(recipe_id, name, description, ingredients, steps)

def read_recipe(recipe_id):
    return get_recipe(recipe_id)
