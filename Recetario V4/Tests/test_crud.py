import unittest
from redis_integration.crud import create_recipe, read_recipe

class TestCRUD(unittest.TestCase):

    def test_create_and_read_recipe(self):
        recipe_id = "1"
        create_recipe(recipe_id, "Tarta de Manzana", "Deliciosa tarta", "manzana, harina", "mezclar y hornear")
        recipe = read_recipe(recipe_id)
        self.assertIsNotNone(recipe)
        self.assertEqual(recipe.get(b'name').decode('utf-8'), "Tarta de Manzana")

if __name__ == '__main__':
    unittest.main()
