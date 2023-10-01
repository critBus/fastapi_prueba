from fastapi.testclient import TestClient
import unittest
from .main import *

client = TestClient(app)
class TestEndpoint(unittest.TestCase):
    def test_process_orders(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

class TestEndpoint_Correcto1(unittest.TestCase):
    def test_process_orders(self):
        response = client.post("/solution",json={
            "orders": [{"id": 1,
                    "item": "Laptop",
                    "quantity": 1,
                    "price": 999.99,
                    "status": "completed"}]
            ,"criterion": "completed"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content,  b'999.99')

class TestEndpoint_Correcto_PorDefecto(unittest.TestCase):
    def test_process_orders(self):
        response = client.post("/solution", json={
"orders": [
{
    "id": 1,
    "item": "Laptop",
    "quantity": 1,
    "price": 999.99,
    "status": "completed"
},
{
    "id": 2,
    "item": "Smartphone",
    "quantity": 2,
    "price": 499.95,
    "status": "pending"
},
{
    "id": 3,
    "item": "Headphones",
    "quantity": 3,
    "price": 99.90,
    "status": "completed"
},
{
    "id": 4,
    "item": "Mouse",
    "quantity": 4,
    "price": 24.99,
    "status": "canceled"
}
],
"criterion": "completed"
})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'1299.69')

class TestEndpoint_Incorrecto_Negativo(unittest.TestCase):
    def test_process_orders(self):
        response = client.post("/solution", json={
            "orders": [{"id": 1,
                        "item": "Laptop",
                        "quantity": -1,
                        "price": 999.99,
                        "status": "completed"}]
            , "criterion": "completed"
        })
        self.assertEqual(response.status_code, 400)

class TestEndpoint_Incorrecto_Faltanta_Atributos(unittest.TestCase):
    def test_process_orders(self):
        response = client.post("/solution", json={
            "orders": [{"id": 1,
                        "item": "Laptop",
                        #"quantity": 1,
                        "price": 999.99,
                        "status": "completed"}]
            , "criterion": "completed"
        })
        self.assertEqual(response.status_code, 422)
