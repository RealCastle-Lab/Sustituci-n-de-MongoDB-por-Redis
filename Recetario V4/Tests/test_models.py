import unittest
from redis_integration.models import add_recipe, get_recipe
from redis_integration.db import get_db

class TestModels(unittest.TestCase):
    def setUp(self):
        # Configurar conexión de prueba a Redis (usar una base de datos diferente para pruebas)
        self.redis = get_db()
        self.redis.flushdb()  # Asegúrate de limpiar la base de datos antes de cada prueba

    def test_add_get_recipe(self):
        # Test para verificar la correcta adición y recuperación de recetas
        recipe_id = "test_recipe_1"
        name = "Gazpacho"
        description = "Sopa fría española"
        ingredients = "Tomate, pimiento, cebolla, ajo, pepino"
        steps = "Mezclar ingredientes, refrigerar por una hora"

        # Añadir la receta al Redis
        add_recipe(recipe_id, name, description, ingredients, steps)

        # Recuperar la receta de Redis
        recipe = get_recipe(recipe_id)

        # Verificar que la receta se recupera correctamente
        self.assertEqual(recipe[b'name'].decode('utf-8'), name)
        self.assertEqual(recipe[b'description'].decode('utf-8'), description)
        self.assertEqual(recipe[b'ingredients'].decode('utf-8'), ingredients)
        self.assertEqual(recipe[b'steps'].decode('utf-8'), steps)

    def tearDown(self):
        # Limpiar la base de datos después de cada prueba
        self.redis.flushdb()

if __name__ == '__main__':
    unittest.main()
