from flask import Flask, request, jsonify
from redis_integration.crud import create_recipe, read_recipe

app = Flask(__name__)

@app.route('/recipes', methods=['POST'])
def add_recipe():
    # Obtener datos de la solicitud
    recipe_data = request.json
    recipe_id = recipe_data.get("id")
    name = recipe_data.get("name")
    description = recipe_data.get("description")
    ingredients = recipe_data.get("ingredients")
    steps = recipe_data.get("steps")

    # Crear la receta en Redis
    create_recipe(recipe_id, name, description, ingredients, steps)
    
    return jsonify({"message": "Receta agregada con éxito"}), 201

@app.route('/recipes/<recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    # Obtener la receta desde Redis
    recipe = read_recipe(recipe_id)
    
    if not recipe:
        return jsonify({"message": "Receta no encontrada"}), 404

    # Formatear la respuesta para que sea comprensible
    recipe_formatted = {
        "id": recipe_id,
        "name": recipe.get(b'name').decode('utf-8'),
        "description": recipe.get(b'description').decode('utf-8'),
        "ingredients": recipe.get(b'ingredients').decode('utf-8'),
        "steps": recipe.get(b'steps').decode('utf-8')
    }

    return jsonify(recipe_formatted), 200

if __name__ == '__main__':
    app.run(debug=True)
