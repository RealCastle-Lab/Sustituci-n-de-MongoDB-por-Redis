import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_recipe(self):
        response = self.app.post('/recipes', json={
            "id": "1",
            "name": "Tarta de Manzana",
            "description": "Deliciosa tarta",
            "ingredients": "manzana, harina",
            "steps": "mezclar y hornear"
        })
        self.assertEqual(response.status_code, 201)

    def test_get_recipe(self):
        response = self.app.get('/recipes/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Tarta de Manzana", str(response.data))

if __name__ == '__main__':
    unittest.main()
